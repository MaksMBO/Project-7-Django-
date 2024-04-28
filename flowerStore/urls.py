from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from users.views import AddToCartView

urlpatterns = [
    # path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('api/products/', include('flower.urls')),
    # path('catalog/', include('catalog.urls')),
    path('api/users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
