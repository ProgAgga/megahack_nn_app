from boilerplate.models import *

option = {'column', 'operator', 'value'}


def validate_options(options):
    pass


def validate_offer(client_id, dealer_id, offer_id):
    client = Client.objects.filter(id=client_id).first()
    dealer = Dealer.objects.filter(id=dealer_id).first()
    offer = Offer.objects.filter(id=offer_id).first()

    if not client or not dealer or not offer:
        return False

    if dealer.id not in offer.dealers:
        return False


