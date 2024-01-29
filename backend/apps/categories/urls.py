from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, CategoryViewSetForAdminOnly

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"admin/categories", CategoryViewSetForAdminOnly)

urlpatterns = [
    path("", include(router.urls)),
]