from rest_framework import serializers
from .models import Product, Banner
from django.conf import settings

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if "image" in representation:
            if instance.image and hasattr(instance.image, "url"):
                domain_name = settings.DOMAIN_NAME
                full_path = domain_name + instance.image.url
                representation['image'] = full_path
            else:
                representation['image'] = None
        else:
            representation['image'] = None
        return representation
        


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"