from django import views as vw
from boilerplate.validations.redismodule import execute_query as redis_query
from boilerplate.models import Source, Client

from boilerplate.validations.sqlmodule import execute_query as query
from boilerplate.validations.offer_validation import run_option
from boilerplate.models import Source


class CheckOffer(vw.View):
    def post(self, request):
        '''source = Source.objects.filter(type="REDIS").first()
        client = Client.objects.filter(id=5).first()
        redis_query(source,'calls',client)'''

        source = Source.objects.filter(type="REDIS").first()
        client = Client.objects.filter(id=5).first()
        redis_query(source, 'calls', client)

        print(run_option(client, 1))