import json

from django import views as vw
from django.http import HttpResponse

from boilerplate.validations.offer_validation import validate_offer


class CheckOffer(vw.View):

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        result = validate_offer(body['client'], body['dealer'], body['offer'])
        return HttpResponse(content=json.dumps({
            'result': result,
            **body
        }))
