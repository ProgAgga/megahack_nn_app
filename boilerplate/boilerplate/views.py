from django import views as vw

from boilerplate.validations.sqlmodule import execute_query as query
from boilerplate.models import Source


class CheckOffer(vw.View):
    def post(self, request):
        pass
