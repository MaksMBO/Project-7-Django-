from rest_framework import serializers
from .models import Flower, Currency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = '__all__'
