from django.views import View
from django.shortcuts import render

from services.flower_manager import get_flower_by_id


class FlowerView(View):
    """
    FlowerView view class.
    """

    @staticmethod
    def get(request, id: int):
        """
        Handles GET requests for viewing individual flowers.
        """
        flower_dict = get_flower_by_id(id)

        context = {"flower_dict": flower_dict, }

        return render(request, 'flower/main.html', context)
