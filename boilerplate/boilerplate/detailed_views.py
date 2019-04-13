from django.http import Http404
from rest_framework import generics as gr
from rest_framework.response import Response

from boilerplate.serializers import *


class ClientDetailView(gr.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'


class SourceDetailView(gr.RetrieveAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    lookup_field = 'id'


class DealerDetailView(gr.RetrieveAPIView):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    lookup_field = 'id'


class ClientDetailView(gr.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'


class OfferDetailView(gr.RetrieveDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response({'result': False})
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['result'] = True
        self.perform_destroy(instance)
        return Response(data)


class OfferOrderDetailView(gr.RetrieveAPIView):
    queryset = OfferOrder.objects.all()
    serializer_class = OfferOrderSerializer
    lookup_field = 'id'


class OptionsDetailView(gr.RetrieveDestroyAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            return Response({'result': False})
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['result'] = True
        self.perform_destroy(instance)
        return Response(data)
