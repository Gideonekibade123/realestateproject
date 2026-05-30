from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create superuser automatically'

    def handle(self, *args, **options):
        if not User.objects.filter(username='Gideon').exists():
            User.objects.create_superuser(
                username='Gideon',
                email='gekibade@gmail.com',
                password='Gideon@1234'
            )
            self.stdout.write('Superuser created!')
        else:
            self.stdout.write('Superuser already exists!')