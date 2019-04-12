from rest_framework import generics as gr

from boilerplate.models import *
from boilerplate.serializers import *


class ClientsListView(gr.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


# mock view, SHOULD BE APIView
class OrdersListView(gr.ListAPIView):
    pass