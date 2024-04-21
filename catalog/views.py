from django.views import View
from django.shortcuts import render

from services.flower_manager import get_paginated_flowers


class Catalog(View):
    @staticmethod
    def get(request):
        page_number = request.GET.get('page')
        page_obj = get_paginated_flowers(per_page=12, page_number=page_number)
        return render(request, 'catalog/main.html', {'page_obj': page_obj,
                                                     "count": request.user.cart_count(),})
