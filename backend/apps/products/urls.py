from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BannerViewSet, ProductViewSet, ProductForUrlListView

router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"banners", BannerViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('gif-url/', ProductForUrlListView.as_view(), name='product-list'),

]
