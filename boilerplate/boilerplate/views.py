from django import views as vw

from boilerplate.validations.sqlmodule import execute_query as query
from boilerplate.models import Source, Client


class CheckOffer(vw.View):
    def post(self, request):
        src = Source.objects.filter(pk=1).get()
        client = Client.objects.filter(pk=1).get()
        query(src, 'age', client)
