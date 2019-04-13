from boilerplate.models import *
from boilerplate.validations.sqlmodule import execute_query


def validate_option_definition(option):
    pass


def run_option(client, option):
    option = Options.objects.filter(pk=option).first()
    # what if None? TODO
    if not option:
        return True
    execute_query(option.sources, 'boilerplate_client',
                  option.options['column'], client)


def validate_offer(client_id, dealer_id, offer_id):
    client = Client.objects.filter(id=client_id).first()
    dealer = Dealer.objects.filter(id=dealer_id).first()
    offer = Offer.objects.filter(id=offer_id).first()
    if not client or not dealer or not offer:
        return False
    if dealer.id not in offer.dealers:
        return False
    for option in offer.options:
        run_option(client, option)



