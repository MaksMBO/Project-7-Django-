from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from flower.models import Flower

class AddToCartView(View):
    def post(self, request, flower_id):
        user = request.user
        flower = get_object_or_404(Flower, pk=flower_id)
        
        if flower in user.cart.all():
            return HttpResponseRedirect(reverse('cart_items')) 
        else:
            user.cart.add(flower)
            user.save()
            return HttpResponseRedirect(reverse('cart_items')) 
        

class RemoveFromCartView(View):
    def post(self, request, flower_id):
        user = request.user
        flower = get_object_or_404(Flower, pk=flower_id)
        
        if flower in user.cart.all():
            user.cart.remove(flower)
            user.save()
        
        return HttpResponseRedirect(reverse('cart_items'))


class CartItemsView(View):
    def get(self, request):
        user = request.user
        items = list(user.cart_items().values())

        return render(request, 'cart/cart.html', context={'items': items,
                             "count": request.user.cart_count(),})
