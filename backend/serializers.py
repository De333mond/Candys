from rest_framework import serializers
from .models import *



class FillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filling
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    available_fillings = FillingSerializer(many=True, read_only=True)
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ["id", "title", "description", "price", "oldPrice", "image", "adv_state", "category", "available_fillings"]


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carousele
        fields = "__all__"


class OrderHasProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHasProduct
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    total_sum = serializers.FloatField(source="get_full_price")
    class Meta: 
        model = Order
        fields = ["id", "delivery_address", "delivery_date", "payment", "pickup", "user",  "total_sum", "products",]

 
class CustromerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["delivery_adress", 'get_emails']


class UserSerializer(serializers.ModelSerializer):
    customer = CustromerSerializer(many=False)
    class Meta:
        model = User
        fields = ['id', 'first_name', "last_name", "email", "customer"]