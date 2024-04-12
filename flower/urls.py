from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.FlowerView.as_view(), name='about_flower'),
]
