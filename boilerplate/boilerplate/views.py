import json

from django import views as vw
from django.http import HttpResponse

from boilerplate.validations.offer_validation import validate_order


class CheckOffer(vw.View):
    """
        create:
            Synchronously check the ability of making offer
    """

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        result, valid, invalid = validate_order(body['client'], body['dealer'], body['offer'])
        return HttpResponse(content=json.dumps({
            'result': result,
            'valid': valid,
            'invalid': invalid,
            **body
        }))
