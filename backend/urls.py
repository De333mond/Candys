from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("products", ProductViewSet)
# router.register("products/on-sale", ProductViewSet)
router.register('categories', CategoryViewSet)
router.register("fillings", FillingViewSet)
router.register("carousel", CarouselViewSet) 
router.register("orders", OrderViewSet)
router.register("orderHasProducts", OrderHasProductViewSet),
router.register("customers", CustomerViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include("djoser.urls")),
    path('auth/', include("djoser.urls.authtoken")),
]
