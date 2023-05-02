from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField()
    firstname = models.CharField(max_length=32)
    secondname = models.CharField(max_length=32)
    thirdname = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.thirdname} {self.firstname[0]}. {self.secondname[0]}."


class OrderHasProduct(models.Model):
    product = models.ForeignKey("Product", on_delete=models.DO_NOTHING)
    order = models.ForeignKey("Order", on_delete=models.DO_NOTHING)
    count = models.IntegerField()
    filling = models.ForeignKey("Filling", on_delete=models.DO_NOTHING)


class Order(models.Model):
    delivery_address = models.CharField(max_length=255)
    delivery_date = models.DateTimeField()
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

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    products = models.ManyToManyField("Product", through=OrderHasProduct)

    def get_full_price(self):
        total = 0
        objs = OrderHasProduct.objects.filter(order_id=self.id)
        for item in objs:
            total += (item.product.price + item.filling.price_delta) * item.count
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

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="back/img/products")

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    available_fillings = models.ManyToManyField(Filling)

    def __str__(self):
        return self.title




