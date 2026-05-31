from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

User = get_user_model()


class Command(BaseCommand):
    help = 'Create or update superuser automatically'

    def handle(self, *args, **options):
        username = os.getenv("DJANGO_SUPERUSER_USERNAME", "Gideon")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "gekibade@gmail.com")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "Gideon@1234")

        user, created = User.objects.get_or_create(username=username)
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)  # ✅ always resets password on deploy
        user.save()

        if created:
            self.stdout.write('Superuser created!')
        else:
            self.stdout.write('Superuser updated!')