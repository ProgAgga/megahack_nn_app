import hashlib

from rest_framework import generics as gr
from rest_framework.response import Response

from boilerplate.models import *
from boilerplate.serializers import *
from rest_framework import mixins as mx


class ClientsListView(gr.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class SourcesListView(gr.ListCreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class OffersListView(gr.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class DealersListView(gr.ListCreateAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class OffersOrdersListView(gr.ListCreateAPIView):
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

        if list(data.keys()) != ['client', 'dealer', 'offer']:
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
        return Response(self.get_serializer_class()(offer_order).data)


class OptionsListView(gr.ListCreateAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer
