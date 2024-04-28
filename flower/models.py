from django.db import models

from services.image_info import handle_image


class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.code


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/')
    available = models.BooleanField(default=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.currency_id:
            self.currency = Currency.objects.get(code='UAH')
        super().save(*args, **kwargs)
        handle_image(self)
