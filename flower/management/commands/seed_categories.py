from django.core.management import BaseCommand

from flower.models import ProductCategory

categories = ["Сезонні квіти", "Весільні букети", "Квіткові горщики", "Садові рослини", "Сувенірні квіти",
              "Квіткові аксесуари", "Квіткові подарункові набори", "Квіткові композиції", "Квіткові декорації",
              "Квіткові інструменти та догляд"
              ]


class Command(BaseCommand):
    help = 'Seed base category'

    def handle(self, *args, **kwargs):
        try:
            [ProductCategory.objects.get_or_create(category_name=category_name) for category_name in categories]
            self.stdout.write(self.style.SUCCESS(f"Категорії успішно створені!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Помилка: {e}. Категорія не створена"))
