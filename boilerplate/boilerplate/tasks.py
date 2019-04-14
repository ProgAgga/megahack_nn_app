import datetime

from boilerplate.celery import app
from boilerplate.validations.offer_validation import validate_order
from boilerplate.models import OfferOrder


@app.task(serializer='json')
def order_offer_validate(order_id):
    offer_order = OfferOrder.objects.filter(id=order_id).first()

    if not offer_order:
        return

    offer_order.status, valid, invalid = validate_order(offer_order.client.id,
                                                        offer_order.dealer.id,
                                                        offer_order.offer.id)

    offer_order.date_processed = datetime.datetime.now()
    offer_order.save()


