from rest_framework import permissions, viewsets
from .serializers import ProductSerializer, ProductCategorySerializer, Currency, CurrencySerializer
from .models import Product, ProductCategory


class BaseViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]


class CategoryViewSet(BaseViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class CurrencyViewSet(BaseViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category_id')
        available = self.request.GET.get('available')

        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        if available is not None:
            queryset = queryset.filter(available=True)
        return queryset
