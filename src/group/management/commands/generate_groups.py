from django.core.management.base import BaseCommand
from group.models import Group


class Command(BaseCommand):
    help = u'Generate groups'

    def add_arguments(self, parser):
        parser.add_argument('num_groups', default=100, type=int)

    def handle(self, *args, **kwargs):
        num_groups = kwargs['num_groups']
        Group.objects.all().delete()

        for _ in range(num_groups):
            Group.generate_group()

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {num_groups} groups'))
