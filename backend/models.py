from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class OrderHasProduct(models.Model):
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, related_name="order_product", null=True)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    count = models.IntegerField()
    filling = models.ForeignKey("Filling", on_delete=models.SET_NULL, default=0, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)


class Order(models.Model):
    delivery_address = models.CharField(max_length=255)
    delivery_date = models.DateTimeField(blank=True)
    payments = (
        ("card", "Банковская карта"),
        ("money", "Наличные")
    )

    pickups = (
        ("delivery", "Доставка"),
        ("pickup", "Самовывоз")
    )
    payment = models.CharField(max_length=5, choices=payments)
    pickup = models.CharField(max_length=8, choices=pickups)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField("Product", through=OrderHasProduct)

    def get_full_price(self):
        total = 0
        objs = OrderHasProduct.objects.filter(order_id=self.id)
        for item in objs:
            item_price = item.product.price
            if (item.filling):
                item_price += item.filling.price_delta

            if (item.title != ""):
                item_price += 200

            total += item_price * item.count
        return total

    def __str__(self):
        return f"[{self.id}] Дата: {self.delivery_date.date()}, Сумма: {self.get_full_price()}"


class Filling(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField(upload_to="back/img/fillings/")
    price_delta = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=32)
    image = models.ImageField(upload_to="back/img/categories/")
    canHaveTitle = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Product(models.Model):
    adv_choices = (
        ("no", "Нет"),
        ("sale", "Акция"),
        ("new", "Новинка"),
    )

    title = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.FloatField(default=0)
    oldPrice = models.FloatField(default=0)
    image = models.ImageField(upload_to="back/img/products")
    adv_state = models.CharField(max_length=4, choices=adv_choices, default="no")

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    available_fillings = models.ManyToManyField(Filling, blank=True)

    def __str__(self):
        return self.title


class Carousele(models.Model):
    image = models.ImageField(upload_to="back/img/slides")


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    delivery_adress = models.CharField(max_length=255, blank=True, null=True)
    get_emails = models.BooleanField()
    birthdate = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username
