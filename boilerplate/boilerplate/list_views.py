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
        serializer = self.get_serializer_class()(data=data)
        print(serializer.is_valid())
        client = Client.objects.filter(id=data['client']).get()
        dealer = Dealer.objects.filter(id=data['dealer']).get()
        offer = Offer.objects.filter(id=data['offer']).get()
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

