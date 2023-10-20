import random
from django.core.management.base import BaseCommand
from faker import Faker
from myapp.models import MyModel

fake = Faker()

class Command(BaseCommand):
    help = 'Populate MyModel with dummy data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating MyModel with dummy data...')

        # Adjust the range based on how many instances you want to create
        for _ in range(10):
            MyModel.objects.create(
                name=fake.name(),
                description=fake.text(),
            )

        self.stdout.write(self.style.SUCCESS('Dummy data populated successfully!'))
