from rest_framework import serializers
from .models import Product, Banner


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    def to_representation(self, instance):
            representation = super().to_representation(instance)
            domain_name = "http://0.0.0.0:8000"
            full_path = domain_name + instance.gif.url
            representation['image'] = full_path
            return representation
        


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"