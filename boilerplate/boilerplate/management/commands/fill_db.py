from django.core.management.base import BaseCommand, CommandError
from boilerplate.models import Client, Offer, Options, Dealer
import datetime
import itertools
import random
import string


class Command(BaseCommand):
    list_of_names = ['Вася', 'Петя', 'Андрей', 'Вова', 'Игорь', 'Никита', 'Вера', 'Надежда']
    list_of_last_names = ['Иванов', 'Петров', 'Сидоров', 'Ульянов', 'Бесчастнов', 'Ковалев', 'Трубов']
    list_of_sex = ['M', 'F', 'NB', None]
    list_of_ages = [19, 23, 26, 56, 92, 14]

    @staticmethod
    def date_generator():
        from_date = datetime.datetime.today()
        while True:
            yield from_date
            from_date = from_date - datetime.timedelta(days=random.randint(1, 1000))

    @staticmethod
    def number_generator():
        return '920' + ''.join(random.choice(string.digits) for _ in range(7))

    def handle(self, *args, **options):
        list_of_dates = list(itertools.islice(self.date_generator(), 10))
        for _ in range(100):
            name = f'{random.choice(self.list_of_names)} {random.choice(self.list_of_last_names)}'
            sex = random.choice(self.list_of_sex)
            age = random.choice(self.list_of_ages)
            date = random.choice(list_of_dates)
            phone = self.number_generator()
            print(phone)
            Client(name=name, sex=sex, age=age, date_of_admission=date, phone=phone).save()
