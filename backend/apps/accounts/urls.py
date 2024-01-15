from django.urls import path
from .views import CustomAuthToken

urlpatterns = [
    path("get_token/", CustomAuthToken.as_view()),
]
