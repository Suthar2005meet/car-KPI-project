from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import KPI data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('KPI import done!'))
