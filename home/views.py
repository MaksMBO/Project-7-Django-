from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from services.subscribe import subscribe_user
from services.flower_manager import get_all_flowers


class Home(View):

    @staticmethod
    def get(request):
        all_flower_dict = get_all_flowers(limit=8, available=True)
        context = {
            "all_flower_dict": all_flower_dict,
        }
        return render(request, 'home/main.html', context)


class Subscribe(View):
    
    @staticmethod
    def post(request):
        email = request.POST.get('email')
        if email is not None:
            subscribe_user(email)
        return HttpResponseRedirect(reverse('home'))
