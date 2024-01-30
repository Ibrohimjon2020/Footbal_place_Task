from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (BannerViewSet, ProductForUrlListView, ProductViewSet,
                    ProductViewSetAdmin)

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"banners", BannerViewSet)
router.register(r"admin/product", ProductViewSetAdmin,basename="admin-products")


urlpatterns = [
    path("", include(router.urls)),
    path("gif-url/", ProductForUrlListView.as_view()),
]
