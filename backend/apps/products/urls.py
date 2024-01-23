from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BannerViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"banners", BannerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
