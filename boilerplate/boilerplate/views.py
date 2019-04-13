import hashlib

from rest_framework import generics as gr
from rest_framework.response import Response

from boilerplate.models import *
from boilerplate.serializers import *


class ClientsListView(gr.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailView(gr.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'


class SourcesListView(gr.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class SourceDetailView(gr.RetrieveAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    lookup_field = 'id'


class OffersListView(gr.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class DealersListView(gr.ListAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class OfferDetailView(gr.RetrieveAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    lookup_field = 'id'


class DealerDetailView(gr.RetrieveAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    lookup_field = 'id'


class ClientDetailView(gr.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'


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


class OfferOrderDetailView(gr.RetrieveAPIView):
    queryset = OfferOrder.objects.all()
    serializer_class = OfferOrderSerializer
    lookup_field = 'id'
