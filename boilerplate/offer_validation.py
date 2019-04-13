from boilerplate.models import *


def validate_offer(client_id, dealer_id, offer_id):
    client = Client.objects.filter(id=client_id).first()
    dealer = Dealer.objects.filter(id=dealer_id).first()
    offer = Offer.objects.filter(id=offer_id).first()

    if not client or not dealer or not offer:
        return False


