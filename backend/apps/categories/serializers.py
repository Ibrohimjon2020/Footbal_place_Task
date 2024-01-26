# serializers.py
from apps.products.models import Product
from django.conf import settings
from rest_framework import serializers

from .models import Category


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
        products = obj.cat_products.all()[:5]
        # Har bir kategoriya uchun 5 mahsulot
        return ProductSerializer(products, many=True).data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        domain_name = settings.DOMAIN_NAME
        if instance.image and hasattr(instance.image, "url"):
            domain_name = settings.DOMAIN_NAME
            full_path = domain_name + instance.image.url
            representation["image"] = full_path
        else:
            representation["image"] = None

        return representation


# CategorySerializer-ni yangilash


class CategoryForChildrenSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

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
            "children",
        ]

    def get_children(self, obj):
        children = Category.objects.filter(parent=obj)
        return CategorySerializer(children, many=True).data


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    parent = CategorySubSerializer(required=False)
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "name_uz",
            "name_ru",
            "description",
            "description_uz",
            "description_ru",
            "title",
            "title_uz",
            "title_ru",
            "image",
            "head_name",
            "head_name_uz",
            "head_name_ru",
            "hashtag_name",
            "hashtag_name_uz",
            "hashtag_name_ru",
            "parent",
            "created",
            "updated",
            "products",
            "children",
            "products_count",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Image URL tekshiruvi
        if instance.image and hasattr(instance.image, "url"):
            domain_name = settings.DOMAIN_NAME
            full_path = domain_name + instance.image.url
            representation["image"] = full_path
        else:
            representation["image"] = None

        return representation

    def get_products_count(self, obj):
        products_count = obj.cat_products.all().count()
        return products_count

    def get_products(self, obj):
        products = obj.cat_products.all()[:5]
        # Har bir kategoriya uchun 5 mahsulot
        return ProductSerializer(products, many=True).data

    def get_children(self, obj):
        children = Category.objects.filter(parent=obj)
        return CategoryForChildrenSerializer(children, many=True).data

class CategoryCreateSerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), required=False
    )
    children = serializers.ListField(write_only=True, required=False)

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
            "children",
        ]

    def create_childeren(self, parent_instance, children_data):
        for child_name in children_data:
            try:
                category_instance = Category.objects.get(name=child_name)
            except Category.DoesNotExist:
                category_instance = Category.objects.create(name=child_name, parent=parent_instance)

    def update(self, instance, validated_data):
        children_data = validated_data.pop("children", [])
        if children_data and children_data != [""]:
            new_data = children_data[0].split(", ")
            instance = super().update(instance, validated_data)
            self.create_childeren(instance, new_data)
        else:
            instance = super().update(instance, validated_data)
        return instance
    
    def create(self, validated_data):
        children_data = validated_data.pop("children", [])
        if children_data and children_data != [""]:
            new_data = children_data[0].split(", ")
            instance = super().create(validated_data)
            self.create_childeren(instance, new_data)
        else:
            instance = super().create(validated_data)
        return instance

