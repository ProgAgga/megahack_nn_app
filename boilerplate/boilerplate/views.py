from rest_framework import generics as gr

from boilerplate.models import *


class ClientsListView(gr.ListAPIView):
    queryset = Client.objects.all()


