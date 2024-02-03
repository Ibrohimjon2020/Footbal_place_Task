from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MaydonListView, MaydonCreateView, MaydonUpdateView, MaydonDeleteView

urlpatterns = [
    path('maydonlar-list/', MaydonListView.as_view(), name='maydon-list'),
    path('maydonlar/', MaydonCreateView.as_view(), name='maydon-list'),
    path('maydonlar/<int:pk>/', MaydonUpdateView.as_view(), name='maydon-update'),
    path('maydonlar-delete/<int:pk>/', MaydonDeleteView.as_view(), name='maydon-delete'),
]