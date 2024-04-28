from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet, CustomAuthToken, CustomTokenRefreshView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api-token-auth'),
    path('api-token-refresh/', CustomTokenRefreshView.as_view(), name='api-token-refresh'),
]
