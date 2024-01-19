# serializers.py
from rest_framework import serializers
from .models import Category
from apps.products.models import Product
from django.conf import settings


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "image",
            "gif",
            "name",
            "price",
            "prepare_time",
            "description",
            "category",
        ]  # Kerakli maydonlarni tanlang

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Ishonchli qiling, modellarda rasm (image) va gif maydonlari mavjud ekanligi
        if "image" in representation:
            if instance.image and hasattr(instance.image, "url"):
                full_path = settings.DOMAIN_NAME + instance.image.url
                representation["image"] = full_path
            else:
                representation["image"] = None

        # 'gif' attributi uchun tekshirish
        if "gif" in representation:
            if instance.gif and hasattr(instance.gif, "url"):
                full_path = settings.DOMAIN_NAME + instance.gif.url
                representation["gif"] = full_path
            else:
                representation["gif"] = None

        return representation


class CategorySubSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "description",
            "title",
            "image",
            "head_name",
            "hashtag_name",
            "created",
            "updated",
            "products",
        ]

    def get_products(self, obj):
        products = Product.objects.filter(category=obj)[
            :5
        ]  # Har bir kategoriya uchun 5 mahsulot
        return ProductSerializer(products, many=True).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        domain_name = settings.DOMAIN_NAME
        full_path = domain_name + instance.image.url
        representation["image"] = full_path
        return representation


# CategorySerializer-ni yangilash
class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    parent = CategorySubSerializer(required=False)

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "description",
            "title",
            "image",
            "head_name",
            "hashtag_name",
            "parent",
            "created",
            "updated",
            "products",
            "children",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        domain_name = settings.DOMAIN_NAME
        full_path = domain_name + instance.image.url
        representation["image"] = full_path
        return representation

    def get_products(self, obj):
        products = Product.objects.filter(category=obj)[
            :5
        ]  # Har bir kategoriya uchun 5 mahsulot
        return ProductSerializer(products, many=True).data

    def get_children(self, obj):
        children = Category.objects.filter(parent=obj)
        return CategorySerializer(children, many=True).data


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "description",
            "title",
            "image",
            "head_name",
            "hashtag_name",
            "parent",
            "created",
            "updated",
        ]
