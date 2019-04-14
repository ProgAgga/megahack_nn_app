from boilerplate.celery import app
from boilerplate.validations.offer_validation import validate_order


@app.task(serializer='json')
def order_offer_validate(order_id):
    pass
