from rest_framework import serializers
from .models import Product, ProductGallery

class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    productgallery_set = ProductGallerySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
