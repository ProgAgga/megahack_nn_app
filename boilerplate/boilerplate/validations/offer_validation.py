from boilerplate.models import *
from boilerplate.validations.redismodule import execute_query as redis_query
from boilerplate.validations.sqlmodule import execute_query as sql_query


def validate_option_definition(option):
    pass


def run_option(client, option):
    option = Options.objects.filter(pk=option).first()
    print(option.description)
    if not option:
        return True
    source = option.sources
    print(source.name)
    if not source:
        return True
    if source.type == 'SQL':
        query = sql_query
    elif source.type == 'REDIS':
        query = redis_query
    print(query)
    try:
        result = query(source, option.options['column'], client)
    except:
        return False
    operator = option.options['operator']
    value = option.options['value']
    # сравнить value и result используя operator
    try:
        if operator == '>':
            return result > value
        elif operator == '==':
            return result == value
        elif operator == '>=':
            return result >= value
        elif operator == '<':
            return result < value
        elif operator == '<=':
            return result <= value
    except TypeError:
        return False


def validate_order(client_id, dealer_id, offer_id):
    client = Client.objects.filter(id=client_id).first()
    dealer = Dealer.objects.filter(id=dealer_id).first()
    offer = Offer.objects.filter(id=offer_id).first()
    if not client or not dealer or not offer:
        return False
    if dealer.id not in offer.dealers:
        return False
    valid = []
    invalid = []
    for option in offer.options:
        passed = run_option(client, option)
        if passed:
            valid.append(option)
        else:
            invalid.append(option)
    if invalid:
        return False, valid, invalid
    else:
        return True, valid, invalid
