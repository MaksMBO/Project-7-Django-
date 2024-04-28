from django.core.management import BaseCommand
from faker import Faker

from flower.management.commands.seed_categories import categories
from flower.management.commands.seed_currencies import currency_codes
from flower.models import Product, Currency, ProductCategory

fake = Faker('uk_UA')


class Command(BaseCommand):
    help = 'Seed fake products'

    def handle(self, *args, **kwargs):

        for i in range(1, 22):
            try:
                name = fake.text(max_nb_chars=20)
                description = fake.text()
                price = fake.pydecimal(left_digits=3, right_digits=2, positive=True)
                currency = Currency.objects.get(code=fake.random_element(elements=currency_codes))
                category = ProductCategory.objects.get(category_name=fake.random_element(elements=categories))
                image_path = f'flowers/flower_{i}.webp'
                available = fake.boolean()

                Product.objects.create(
                    name=name,
                    description=description,
                    price=price,
                    currency=currency,
                    category=category,
                    image=image_path,
                    available=available
                )
                self.stdout.write(self.style.SUCCESS(f"Продукт {name} {price} {currency} успішно створений!"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Помилка: {e}. Продукт не створений"))

        self.stdout.write(self.style.SUCCESS(f"Продукти успішно створені!"))
