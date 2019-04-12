from django.core.management.base import BaseCommand
from boilerplate.models import Dealer


class Command(BaseCommand):
    list_of_names = ['Связной', 'Академия Честности', 'Вася и Ко', 'Антихард', 'Империя Грез Мир Труд Май']

    def handle(self, *args, **options):
        for name in self.list_of_names:
            Dealer(name=name).save()
