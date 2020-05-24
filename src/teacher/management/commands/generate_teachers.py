from django.core.management.base import BaseCommand
from teacher.models import Teacher


class Command(BaseCommand):
    help = u'Generate N fake teachers'

    def add_arguments(self, parser):
        parser.add_argument('num_teachers', default=25, type=int)

    def handle(self, *args, **kwargs):
        num_teachers = kwargs['num_teachers']
        Teacher.objects.all().delete()

        for _ in range(num_teachers):
            Teacher.generate_teacher()

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {num_teachers} teachers'))
