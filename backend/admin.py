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


"""
---Admin models---
"""
# Register your models here.
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


admin.site.register(Category)
admin.site.register(Filling)
admin.site.register(User)
admin.site.register(Carousele)



