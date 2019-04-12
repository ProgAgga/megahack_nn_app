from django.core.management.base import BaseCommand
from boilerplate.models import Offer, Client, Dealer

import datetime
import random


class Command(BaseCommand):
    list_of_names = []

    @staticmethod
    def date_generator():
        from_date = datetime.datetime.today()
        while True:
            yield from_date
            from_date = from_date - datetime.timedelta(days=random.randint(1, 10))

    def handle(self, *args, **options):
        for name in self.list_of_names:
            date_created = self.date_generator()
            date_processed = date_created + datetime.timedelta(days=random.randint(1, 10))
