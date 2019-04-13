from django.core.management.base import BaseCommand
from boilerplate.models import Source, SourceTypeChoices


class Command(BaseCommand):
    list_of_types = [x[0] for x in SourceTypeChoices.CHOICES]
    list_of_names = ['База данных пользователей', 'Хранилище звонков', 'API Налоговой']
    list_of_ports = [5432, 6379, 80]
    list_of_hosts = ['localhost', 'localhost', 'api.nalog.org']
    list_of_usernames = ['username', None, 'ploti']
    list_of_passwords = ['password', None, 'hispassword']
    list_of_databases = ['main', '0', '']
    list_of_tables = ['boilerplate_client', None, None]

    def handle(self, *args, **options):
        for type_, name, port, host, username, password, database, table in zip(self.list_of_types,
                                                                                self.list_of_names,
                                                                                self.list_of_ports,
                                                                                self.list_of_hosts,
                                                                                self.list_of_usernames,
                                                                                self.list_of_passwords,
                                                                                self.list_of_databases,
                                                                                self.list_of_tables):
            Source(name=name, type=type_, port=port,
                   host=host, username=username, password=password, database=database, table=table).save()
