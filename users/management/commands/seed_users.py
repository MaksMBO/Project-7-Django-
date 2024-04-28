from django.core.management import BaseCommand
from django.db import IntegrityError
from faker import Faker

from users.models import CustomUser

fake = Faker()


class Command(BaseCommand):
    help = 'Seed fake users'

    def handle(self, *args, **kwargs):

        for _ in range(10):
            email = fake.email()
            password = fake.password()
            try:
                user = CustomUser.objects.create(email=email)
                user.set_password(password)
                user.save()
                self.stdout.write(self.style.SUCCESS(f"Створено користувача з email {email}"))
            except IntegrityError:
                self.stdout.write(self.style.ERROR(f"Email {email} вже існує, спробуйте інший."))
        self.stdout.write(self.style.SUCCESS(f"Користувачі успішно створені!"))
