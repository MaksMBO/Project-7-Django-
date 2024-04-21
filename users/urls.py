from django.urls import path
from . import views 

urlpatterns = [
    path('add-to-cart/<int:flower_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<int:flower_id>/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('cart-items/', views.CartItemsView.as_view(), name='cart_items'),
]