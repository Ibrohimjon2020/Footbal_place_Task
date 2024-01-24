from django.conf import settings
from rest_framework import serializers

from .models import Banner, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.image and hasattr(instance.image, "url"):
            domain_name = settings.DOMAIN_NAME
            full_path = domain_name + instance.image.url
            representation["image"] = full_path
        else:
            representation["image"] = None

        return representation


class ProductSerializerForUrl(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id","gif"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.gif and hasattr(instance.gif, "url"):
            domain_name = settings.DOMAIN_NAME
            full_path = domain_name + instance.gif.url
            representation["gif"] = full_path
        else:
            representation["gif"] = None

        return representation



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
