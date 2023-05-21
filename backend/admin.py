from django.contrib import admin
from .models import *

"""
---Inlines---
"""
class OrderHasProductInline(admin.TabularInline):
    model = OrderHasProduct


"""
---Actions---
"""

@admin.action(description="Set products on sale")
def markOnSale(modeladmin, request, queryset):
    queryset.update(adv_state='sale')


@admin.action(description="Set products on new")
def markOnSale(modeladmin, request, queryset):
    queryset.update(adv_state='new')

"""
---Admin models---
"""

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "price", 'adv_state', "category"]
    list_filter = ["category"]
    actions = [markOnSale]



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Order._meta.fields] + ["order_full_price"]
    inlines = [OrderHasProductInline]

    def order_full_price(self, obj):
        return obj.get_full_price()


@admin.register(Filling)
class FillingAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


@admin.register(Customer)
class Custromer(admin.ModelAdmin):
    list_display = [f.name for f in Customer._meta.fields]
    

admin.site.register(Category)
admin.site.register(Carousele)
admin.site.register(OrderHasProduct)



