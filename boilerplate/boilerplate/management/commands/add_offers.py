from django.core.management.base import BaseCommand
from boilerplate.models import Offer

import datetime
import random


class Command(BaseCommand):
    list_of_names = ['Безлимит', '+1 гб интернета', '10 звонков', '200 смс', 'Роуминг дешевле']
    options = []

    @staticmethod
    def date_generator():
        from_date = datetime.datetime.today()
        while True:
            yield from_date
            from_date = from_date + datetime.timedelta(days=random.randint(1, 1000))

    def handle(self, *args, **options):
        for name in self.list_of_names:
            due_date = self.date_generator()
            Offer(name=name, due_date=due_date, options=options).save()
