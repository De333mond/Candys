from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FillingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Filling.objects.all()
    serializer_class = FillingSerializer

# class CategoryAllApiView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


