from django.conf import settings
from rest_framework import serializers

from .models import Banner, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = "__all__"
        fields = (
            "id",
            "image",
            "gif",
            "name",
            "description",
            "price",
            "created",
            "updated",
            "prepare_time",
            "is_active",
            "category",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.image and hasattr(instance.image, "url"):
            domain_name = settings.DOMAIN_NAME
            full_path = domain_name + instance.image.url
            representation["image"] = full_path
        else:
            representation["image"] = None

        if instance.gif and hasattr(instance.gif, "url"):
            domain_name = settings.DOMAIN_NAME
            full_path = domain_name + instance.gif.url
            representation["gif"] = full_path
        else:
            representation["gif"] = None

        return representation


class ProductSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = "__all__"
        fields = (
            "id",
            "image",
            "gif",
            "name",
            "name_uz",
            "name_ru",
            "description",
            "description_uz",
            "description_ru",
            "price",
            "created",
            "updated",
            "prepare_time",
            "is_active",
            "category",
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.image and hasattr(instance.image, "url"):
            domain_name = settings.DOMAIN_NAME
            full_path = domain_name + instance.image.url
            representation["image"] = full_path
        else:
            representation["image"] = None

        if instance.gif and hasattr(instance.gif, "url"):
            domain_name = settings.DOMAIN_NAME
            full_path = domain_name + instance.gif.url
            representation["gif"] = full_path
        else:
            representation["gif"] = None

        return representation


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "image",
            "gif",
            "name",
            "name_uz",
            "name_ru",
            "description",
            "description_uz",
            "description_ru",
            "price",
            "created",
            "updated",
            "prepare_time",
            "is_active",
            "category",
        )


class ProductSerializerForUrl(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "gif"]

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
        fields = ("id", "title", "summary", "image", "video", "body", "is_active")


class BannerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
