from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('subscribe/', views.Subscribe.as_view(), name="subscribe")
]
