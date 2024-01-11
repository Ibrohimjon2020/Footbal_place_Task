from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductGalleryViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'productgallery', ProductGalleryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]