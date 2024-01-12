from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets
from .models import Product, ProductGallery
from .serializers import ProductSerializer, ProductGallerySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductGalleryViewSet(viewsets.ModelViewSet):
    queryset = ProductGallery.objects.all()
    serializer_class = ProductGallerySerializer
