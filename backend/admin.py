from django.contrib import admin
from .models import *


class OrderHasProductInline(admin.TabularInline):
    model = OrderHasProduct


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Product._meta.fields]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Order._meta.fields] + ["order_full_price"]
    inlines = [OrderHasProductInline]

    def order_full_price(self, obj):
        return obj.get_full_price()


admin.site.register(Category)
admin.site.register(Filling)
admin.site.register(User)
