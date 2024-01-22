# serializers.py
from rest_framework import serializers
from .models import Category
from apps.products.models import Product
from django.conf import settings
from apps.accounts.permissions import IsOwnerOrReadonly


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
        products  = obj.cat_products.all()[
            :5
        ] 
        # Har bir kategoriya uchun 5 mahsulot
        return ProductSerializer(products, many=True).data

    def get_children(self, obj):
        children = Category.objects.filter(parent=obj)
        return CategoryForChildrenSerializer(children, many=True).data
    
    def validate(self, data):
        request = self.context['request']
        instance = self.instance
        
        # Permission check using IsOwnerOrReadonly
        if instance and not IsOwnerOrReadonly().has_object_permission(request, None, instance):
            raise serializers.ValidationError("You don't have permission to modify this object.")

        return data
        


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
