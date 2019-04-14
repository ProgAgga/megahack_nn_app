import json

from django import views as vw
from django.http import HttpResponse

from boilerplate.validations.offer_validation import validate_order


class CheckOffer(vw.View):
    """
        create:
            Check the ability of making offer
    """

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        result = validate_order(body['client'], body['dealer'], body['offer'])
        return HttpResponse(content=json.dumps({
            'result': result,
            **body
        }))
