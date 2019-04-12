from django.core.management.base import BaseCommand
from boilerplate.models import Source, SourceTypeChoices


class Command(BaseCommand):
    list_of_types = [x[0] for x in SourceTypeChoices.CHOICES]
    list_of_names = ['База данных пользователей', 'Хранилище звонков', 'API Налоговой']
    list_of_ports = [5432, 6379, 80]
    list_of_hosts = ['localhost', 'vm01calls', 'api.nalog.org']
    list_of_usernames = ['username', 'callman', 'ploti']
    list_of_passwords = ['password', 'mypassword', 'hispassword']
    list_of_databases = ['main', 'calls', '']

    def handle(self, *args, **options):
        for type_, name, port, host, username, password, database in zip(self.list_of_types,
                                                                         self.list_of_names,
                                                                         self.list_of_ports,
                                                                         self.list_of_hosts,
                                                                         self.list_of_usernames,
                                                                         self.list_of_passwords,
                                                                         self.list_of_databases):
            Source(name=name, type=type_, port=port,
                   host=host, username=username, password=password, database=database).save()
