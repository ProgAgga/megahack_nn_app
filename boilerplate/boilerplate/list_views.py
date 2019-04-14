import hashlib

from rest_framework import generics as gr
from rest_framework.response import Response

from boilerplate.serializers import *
from boilerplate.tasks import order_offer_validate


class ClientsListView(gr.ListCreateAPIView):
    """
        Clients
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class SourcesListView(gr.ListCreateAPIView):
    """
        Sources - databases
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class OffersListView(gr.ListCreateAPIView):
    """
        Offers
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class DealersListView(gr.ListCreateAPIView):
    """
        Dealers
    """
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class OffersOrdersListView(gr.ListCreateAPIView):
    """
        Pool of Orders
    """
    queryset = OfferOrder.objects.all()
    serializer_class = OfferOrderSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        if data.get('client') is None or data.get('dealer') is None or data.get('offer') is None:
            return Response({'error': 'Provide all fields'})
        client = Client.objects.filter(id=data['client']).first()
        dealer = Dealer.objects.filter(id=data['dealer']).first()
        offer = Offer.objects.filter(id=data['offer']).first()

        response = dict()
        if not client:
            response['client'] = f"Object with id = {data['client']} does not exist"
        if not dealer:
            response['dealer'] = f"Object with id = {data['dealer']} does not exist"
        if not offer:
            response['offer'] = f"Object with id = {data['offer']} does not exist"

        if set(data.keys()) != {'client', 'dealer', 'offer'}:
            response['error'] = "Only 'client', 'dealer', 'offer' should be included in request"

        if response:
            return Response(response)

        id_hash = hashlib.sha256(f'{client}{dealer}{offer}'.encode()).hexdigest()
        offer_order = OfferOrder(
            offer=offer,
            client=client,
            dealer=dealer,
            id_hash=id_hash,
            status='P'
        )
        offer_order.save()
        order_offer_validate(offer_order.id)
        return Response(self.get_serializer_class()(offer_order).data)


class OptionsListView(gr.ListCreateAPIView):
    """
        Options - criteria for adding offer
    """
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer
