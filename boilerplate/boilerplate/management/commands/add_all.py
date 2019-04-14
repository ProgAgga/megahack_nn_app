from django.core.management.base import BaseCommand

from .add_clients import Command as AddClients
from .add_dealers import Command as AddDealers
from .add_offers import Command as AddOffers
from .add_offers_orders import Command as AddOffersOrders
from .add_options import Command as AddOptions
from .add_sources import Command as AddSources


class Command(BaseCommand):

    def handle(self, *args, **options):
        AddDealers().handle()
        AddClients().handle()
        AddSources().handle()
        AddOptions().handle()
        AddOffers().handle()
        AddOffersOrders().handle()


