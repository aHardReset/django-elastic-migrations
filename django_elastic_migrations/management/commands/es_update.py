from django.core.management import call_command

from django_elastic_migrations import DEMIndexManager
from django_elastic_migrations.management.commands.es import ESCommand


class Command(ESCommand):
    help = "django-elastic-migrations: update an index"

    def add_arguments(self, parser):
        parser.add_argument(
            'index', nargs='+',
            help='Name of an index'
        )
        parser.add_argument(
            "-ls", "--list-available", action='store_true',
            help='List the available named indexes'
        )

    def handle(self, *args, **options):
        if options.get('list_available'):
            call_command('es_list')
        indexes_to_create = options.get('index', [])
        if indexes_to_create:
            for index_name in indexes_to_create:
                DEMIndexManager.update_index(index_name)
        breakpoint = None
