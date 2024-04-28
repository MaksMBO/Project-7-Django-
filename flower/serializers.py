from rest_framework import serializers
from .models import Product, ProductCategory, Currency


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'category_name']


class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'currency', 'image', 'available', 'category']


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'code']
