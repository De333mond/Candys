import requests
from django.http import JsonResponse
from django.views import View
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import *


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

    @action(methods=['GET'], detail=True)
    def get_qr(self, request, pk=None):
        API_URL = 'https://api.qrserver.com/v1/create-qr-code/'
        payload = f'https://candys.ru/item/{pk}'

        params = {'size': '150x150', 'data': payload}

        response = requests.get(API_URL, params=params)

        if response.status_code == 200:
            qr_code_url = response.url
            return Response({'qr_code_url': qr_code_url})
        else:
            return Response(
                {'error': 'Failed to generate QR code'},
                status=response.status_code)




class CategoryView(View):
    @staticmethod
    def serialize(category: Category) -> dict:
        return {
            'id': category.id,
            'title': category.title,
            'image': "http://127.0.0.1:8000" + category.image.url,
            'canHaveTitle': category.canHaveTitle,
        }


    def get(self, request, category_id=None):
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
                return JsonResponse(self.serialize(category))
            except Category.DoesNotExist:
                return JsonResponse({'error': 'Category not found'}, status=404)
        else:
            categories = Category.objects.all()
            return JsonResponse([self.serialize(el) for el in categories], safe=False)


    def post(self, request):
        title = request.POST.get('title')
        image = request.FILES.get('image')
        canHaveTitle = request.POST.get('canHaveTitle') == 'true'

        category = Category.objects.create(
            title=title,
            image=image,
            canHaveTitle=canHaveTitle
        )

        return JsonResponse(self.serialize(category), status=201)


    def put(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
            category.title = request.POST.get('title', category.title)
            category.image = request.FILES.get('image', category.image)
            category.canHaveTitle = request.POST.get(
                'canHaveTitle',
                category.canHaveTitle) == 'true'

            category.save()

            return JsonResponse(self.serialize(category))

        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category not found'}, status=404)


    def delete(self, request, category_id):
        try:
            category = Category.objects.get(id=category_id)
            category.delete()
            return JsonResponse(
                {'message': 'Category deleted successfully'}, status=204)
        except Category.DoesNotExist:
            return JsonResponse(
                {'error': 'Category not found'}, status=404)


class FillingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Filling.objects.all()
    serializer_class = FillingSerializer


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
    queryset = OrderHasProduct.objects.all()
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
