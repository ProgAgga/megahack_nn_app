from boilerplate.redis_database import redis_db
import json
from django.http import Http404
from rest_framework import generics as gr
from rest_framework.response import Response

from boilerplate.serializers import *


class ClientDetailView(gr.RetrieveAPIView):
    """
        Get Client by ID
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'


class SourceDetailView(gr.RetrieveAPIView):
    """
        Get Source by ID
    """
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    lookup_field = 'id'


class DealerDetailView(gr.RetrieveAPIView):
    """
        Get Dealer by ID
    """
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
    lookup_field = 'id'


class ClientDetailView(gr.RetrieveAPIView):
    """
        Get Client by ID
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'


class OfferDetailView(gr.RetrieveDestroyAPIView):
    """
        Offer by ID
    """
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
    """
        Get Offer by ID
    """
    queryset = OfferOrder.objects.all()
    serializer_class = OfferOrderSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Http404:
            raise
        serializer = self.get_serializer(instance)
        data = serializer.data
        if instance.status != 'P':
            valid = redis_db.get(f'{instance.id}_valid')
            if valid is not None:
                valid = json.loads(valid)
            invalid = redis_db.get(f'{instance}_invalid')
            if invalid is not None:
                invalid = json.loads(invalid)
            data['valid'] = valid
            data['invalid'] = invalid
        return Response(data)


class OptionsDetailView(gr.RetrieveDestroyAPIView):
    """
        Option by ID
    """
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
