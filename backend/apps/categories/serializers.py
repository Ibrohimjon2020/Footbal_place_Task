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
            # "name_uz",
            # "name_ru",
            "description",
            # "description_uz",
            # "description_ru",
            "title",
            # "title_uz",
            # "title_ru",
            "image",
            "head_name",
            # "head_name_uz",
            # "head_name_ru",
            "hashtag_name",
            # "hashtag_name_uz",
            # "hashtag_name_ru",
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


class CategorySerializerForAdminOnly(serializers.ModelSerializer):
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
            "image",
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
            "children",
        ]

    def to_internal_value(self, data):
        import json

        children_data = data.get("children")
        if children_data:
            try:
                children_data = json.loads(children_data)
                print(children_data, "updat kirdi")
                data.setlist("children", children_data)
            except json.JSONDecodeError:
                raise serializers.ValidationError({"children": "Invalid JSON format"})

        return super().to_internal_value(data)

    def create(self, validated_data):
        children_data = validated_data.pop("children", [])
        category = Category.objects.create(**validated_data)

        for child_data in children_data:
            # Yangi bolalar kategoriyasini yaratish
            child = Category.objects.create(**child_data, parent=category)

        return category

    def update(self, instance, validated_data):
        children_data = validated_data.pop("children", [])
        print(children_data, "updated")
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        for child_data in children_data:
            child_id = child_data.pop("id", None)
            if child_id:
                # Mavjud childni yangilash
                child = Category.objects.get(id=child_id)
                for attr, value in child_data.items():
                    setattr(child, attr, value)
                child.parent = instance
                child.save()
                # existing_child_ids.remove(child_id)
            else:
                # Yangi childni yaratish
                Category.objects.create(**child_data, parent=instance)

        return instance


class CategoryParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "title",
            "image",
            "created",
            "updated",
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
