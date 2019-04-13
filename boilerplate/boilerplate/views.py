from django import views as vw
from boilerplate.validations.redismodule import execute_query as redis_query
from boilerplate.models import Source, Client


class CheckOffer(vw.View):
    def post(self, request):
        source = Source.objects.filter(type="REDIS").first()
        client = Client.objects.filter(id=1).first()
        redis_query(source,'age',client)
