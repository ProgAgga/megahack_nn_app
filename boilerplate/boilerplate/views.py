from rest_framework import generics as gr

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


# mock view, SHOULD BE APIView
class OrdersListView(gr.ListAPIView):
    pass
