"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from .scheme import swagger_urlpatterns


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    # path("sentry-debug/", trigger_error),
    path("admin/", admin.site.urls),
    # Auth
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/account/", include("apps.accounts.urls")),
    path("api/v1/product/", include("apps.products.urls")),
    path("api/v1/category/", include("apps.categories.urls")),
    # path("gettoken/", CustomAuthToken.as_view()),
] + swagger_urlpatterns

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
