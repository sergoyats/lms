from django.core.management.base import BaseCommand
from student.models import Student


class Command(BaseCommand):
    help = u'Generate N fake students'

    def add_arguments(self, parser):
        parser.add_argument('N', type=int, help=u'The number of fake students.')

    def handle(self, *args, **kwargs):
        for _ in range(kwargs['N']):
            Student.generate_student()
