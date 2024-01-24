from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BannerViewSet, ProductViewSet, ProductForUrlViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"banners", BannerViewSet)
router.register(r"gir-url", ProductForUrlViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
