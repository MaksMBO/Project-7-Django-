from django.views import View
from django.shortcuts import render

from services.flower_manager import get_flower_by_id


class FlowerView(View):

    @staticmethod
    def get(request, id: int):
        flower_dict = get_flower_by_id(id)

        context = {"flower_dict": flower_dict,
                   "count": request.user.cart_count(),}

        return render(request, 'flower/main.html', context)




# from rest_framework import status
# from rest_framework import generics
# from .models import Flower, Currency
# from .serializers import FlowerSerializer, CurrencySerializer

# from rest_framework.response import Response


# class FlowerListCreate(generics.ListCreateAPIView):
#     queryset = Flower.objects.all()
#     serializer_class = FlowerSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# class FlowerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Flower.objects.all()
#     serializer_class = FlowerSerializer
