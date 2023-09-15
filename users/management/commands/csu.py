from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@sky.pro3',
            first_name='admin1',
            last_name='SkyPro',
            is_staff=False,
            is_superuser=True
        )

        user.set_password('123')
        user.save()
