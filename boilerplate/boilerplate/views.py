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


# mock view, SHOULD BE APIView
class OrdersListView(gr.ListAPIView):
    pass