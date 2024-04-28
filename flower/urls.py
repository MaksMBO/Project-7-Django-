from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, CurrencyViewSet

router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
