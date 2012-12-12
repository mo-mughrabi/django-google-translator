from django.core.management.base import BaseCommand, CommandError
from _utils import Google

class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        print Google()
        self.stdout.write('Successfully closed poll ' )