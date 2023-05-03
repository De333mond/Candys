from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import action  
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=['GET'], detail=False)
    def on_sale(self, request):
        limit = request.GET.get('limit')
        queryset = Product.objects.filter(adv_state="sale")

        if (limit is not None):
            queryset = queryset[:int(limit)]

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FillingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Filling.objects.all()
    serializer_class = FillingSerializer

# class CategoryAllApiView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


class CarouselViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Carousele.objects.all()
    serializer_class = CarouselSerializer