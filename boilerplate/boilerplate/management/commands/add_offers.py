from django.core.management.base import BaseCommand
from django.db import IntegrityError

from boilerplate.models import Offer, Options

import datetime
import random


class Command(BaseCommand):
    list_of_names = ['Безлимит', '+1 гб интернета', '10 звонков', '200 смс', 'Роуминг дешевле']
    list_of_options = Options.objects.all().values('id')

    @staticmethod
    def date_generator():
        from_date = datetime.datetime.now()
        return from_date + datetime.timedelta(days=random.randint(1, 1000))

    def handle(self, *args, **options):
        for name in self.list_of_names:
            due_date = self.date_generator()
            options_id = random.choice(self.list_of_options)['id']
            try:
                Offer(name=name, due_date=due_date, options=[options_id]).save()
            except IntegrityError:
                pass
