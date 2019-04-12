from django.core.management.base import BaseCommand
from boilerplate.models import OfferOrder, Offer, Client, Dealer, OfferOrderResultChoices

import datetime
import random
import hashlib


class Command(BaseCommand):
    list_of_dealers = Dealer.objects.all().values('id')
    list_of_offers = Offer.objects.all().values('id')
    list_of_clients = Client.objects.all().values('id')
    list_of_results = [x[1] for x in OfferOrderResultChoices.CHOICES]

    @staticmethod
    def date_generator():
        from_date = datetime.datetime.today()
        return from_date - datetime.timedelta(days=random.randint(1, 10))

    def handle(self, *args, **options):
        for _ in range(10):
            date_created = self.date_generator()
            result = random.choice(self.list_of_results)
            if result != OfferOrderResultChoices.PENDING:
                date_processed = date_created + datetime.timedelta(days=random.randint(1, 10))
            else:
                date_processed = None
            client = Client.objects.filter(id=random.choice(self.list_of_clients)['id']).get()
            dealer = Dealer.objects.filter(id=random.choice(self.list_of_dealers)['id']).get()
            offer = Offer.objects.filter(id=random.choice(self.list_of_offers)['id']).get()
            id_hash = hashlib.sha256(f'{client}{dealer}{offer}'.encode()).hexdigest()
            OfferOrder(
                offer=offer,
                client=client,
                dealer=dealer,
                id_hash=id_hash,
                date_created=date_created,
                date_processed=date_processed,
                result=result
            ).save()


