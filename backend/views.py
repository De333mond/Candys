from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.decorators import action  
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser




class ProductViewSet(viewsets.ReadOnlyModelViewSet):
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



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=['GET'], detail=False)
    def by_user(self, request):
        queryset = Order.objects.filter(user_id=request.GET.get('id'))
    
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class OrderHasProductViewSet(viewsets.ModelViewSet):
    queryset =OrderHasProduct.objects.all() 
    serializer_class = OrderHasProductSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustromerSerializer
    permission_classes = [IsAuthenticated]



