from django.core.management import BaseCommand

from flower.models import Currency

currency_codes = ['UAH', 'USD', 'EUR']


class Command(BaseCommand):
    help = 'Seed base currency'

    def handle(self, *args, **kwargs):
        try:
            [Currency.objects.get_or_create(code=code) for code in currency_codes]
            self.stdout.write(self.style.SUCCESS(f"Валюти успішно створені!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Помилка {e}. Валюта не створена"))
