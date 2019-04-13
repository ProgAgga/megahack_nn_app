from django.core.management.base import BaseCommand
from django.db import IntegrityError

from redis import Redis
from boilerplate.models import Client

import datetime
import random


class Command(BaseCommand):

    list_of_columns = ['calls', 'sms', 'gb']

    def handle(self, *args, **options):
        for client in Client.objects.all():
            r = Redis(host='localhost', port=6379, db='0')
            for column in self.list_of_columns:
                r.hset(client.id, column, random.randint(1, 1000))
