from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.FlowerView.as_view(), name='about_flower'),
]

# from django.urls import path
# from .views import FlowerListCreate, FlowerRetrieveUpdateDestroy

# urlpatterns = [
#     path('flowers/', FlowerListCreate.as_view(), name='flower-list-create'),
#     path('flowers/<int:pk>/', FlowerRetrieveUpdateDestroy.as_view(), name='flower-detail'),
# ]
