from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from faker import Faker


from services.image_info import handle_image


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.code


@receiver(post_migrate)
def create_currencies(sender, **kwargs):
    Currency.objects.get_or_create(code='UAH')
    Currency.objects.get_or_create(code='USD')
    Currency.objects.get_or_create(code='EUR')

    faker = Faker()

    for i in range(1, 10):  
        name = faker.name()
        description = faker.text()
        price = faker.pydecimal(left_digits=3, right_digits=2, positive=True)
        currency = Currency.objects.get(code=faker.random_element(elements=['UAH', 'USD', 'EUR']))
        image_path = f'flowers/flower_00{i}.webp'
        available = faker.boolean()

        Flower.objects.create(
            name=name,
            description=description,
            price=price,
            currency=currency,
            image=image_path,
            available=available
        )


class Flower(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='flowers/')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.currency_id:
            self.currency = Currency.objects.get(code='UAH')
        super().save(*args, **kwargs)
        handle_image(self)
