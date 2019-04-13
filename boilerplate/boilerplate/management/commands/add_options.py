from django.core.management.base import BaseCommand
from boilerplate.models import Options, Source

import datetime
import random

# option = {'column', 'operator', 'value'}


class Command(BaseCommand):
    list_of_columns = ['age', 'date_of_admission', 'sex']
    list_of_operators = ['>', '>=', '==']
    list_of_values = ['18', '0:3:0', 'M']
    list_of_sources = Source.objects.all().values('id')
    list_of_descriptions = ['Совершеннолетний', 'Больше трех месяцев', 'Мужчина']

    def handle(self, *args, **options):
        list_of_options = []
        for cl, op, vl in zip(self.list_of_columns,
                              self.list_of_operators,
                              self.list_of_values):
            list_of_options.append({'column': cl, 'operator': op, 'value': vl})

        for ds, opt in zip(self.list_of_descriptions,
                           list_of_options):
            source_id = random.choice(self.list_of_sources)['id']
            source = Source.objects.filter(id=source_id).get()
            Options(description=ds, options=opt, sources=source).save()


