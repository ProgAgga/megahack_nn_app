import os
import random

from django.core.management.base import BaseCommand
from redis import Redis

from boilerplate.models import Client


class Command(BaseCommand):

    list_of_columns = ['calls', 'sms', 'gb']

    def handle(self, *args, **options):
        if not os.getenv('DOCKERED', False):
            r = Redis(host='localhost', port=6379, db='0')
        else:
            r = Redis(host='red', port=6379, db='0')
        for client in Client.objects.all():
            for column in self.list_of_columns:
                r.hset(client.id, column, random.randint(1, 1000))
