from boilerplate.redis_database import redis_db
import datetime
import json

from boilerplate.celery import app
from boilerplate.validations.offer_validation import validate_order
from boilerplate.models import OfferOrder


@app.task(serializer='json')
def order_offer_validate(order_id):
    offer_order = OfferOrder.objects.filter(id=order_id).first()
    if not offer_order:
        return
    status, valid, invalid = validate_order(offer_order.client.id,
                                            offer_order.dealer.id,
                                            offer_order.offer.id)
    if status:
        offer_order.status = 'S'
    else:
        offer_order.status = 'F'
    offer_order.date_processed = datetime.datetime.now()
    offer_order.save()
    redis_db.set(f'{order_id}_valid', json.dumps(valid))
    redis_db.set(f'{order_id}_invalid', json.dumps(invalid))


