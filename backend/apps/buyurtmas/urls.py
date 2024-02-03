from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BuyurtmaListView, BuyurtmaCreateView, BuyurtmaUpdateView, BuyurtmaDeleteView

urlpatterns = [
    path('buyurtmalar-list/', BuyurtmaListView.as_view(), name='buyurtma-list'),
    path('buyurtmalar/', BuyurtmaCreateView.as_view(), name='buyurtma-list'),
    path('buyurtmalar/<int:pk>/', BuyurtmaUpdateView.as_view(), name='buyurtma-update'),
    path('buyurtmalar-delete/<int:pk>/', BuyurtmaDeleteView.as_view(), name='buyurtma-delete'),

]