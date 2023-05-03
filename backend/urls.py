from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("products", ProductViewSet)
router.register('categories', CategoryViewSet)
router.register("fillings", FillingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
