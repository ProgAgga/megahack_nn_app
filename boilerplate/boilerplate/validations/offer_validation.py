from boilerplate.models import *
from boilerplate.validations.sqlmodule import execute_query as sql_query
from boilerplate.validations.redismodule import execute_query as redis_query

def validate_option_definition(option):
    pass

def run_option(client, option):
    option = Options.objects.filter(pk=option).first()
    # what if None? TODO
    if not option:
        return True
    source = Source.objects.filter(pk=option.sources).first()
    if not source:
        return True
    if source.type == 'SQL':
        sql_query(source, 'boilerplate_client',
                      option.options['column'], client)
    elif source.type == 'REDIS':
        redis_query(source, 'boilerplate_client',
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
