from rest_framework import generics as gr

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

