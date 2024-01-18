# serializers.py
from rest_framework import serializers
from .models import Category
from apps.products.models import Product


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

class CategorySubSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ["id", "name", "description", "title", "image", "head_name", "hashtag_name", "created", "updated", "products"]
    
    def get_products(self, obj):
        products = Product.objects.filter(category=obj)[
            :5
        ]  # Har bir kategoriya uchun 5 mahsulot
        return ProductSerializer(products, many=True).data

# CategorySerializer-ni yangilash
class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    parent = CategorySubSerializer(required=False)
    class Meta:
        model = Category
        fields = ["id", "name", "description", "title", "image", "head_name", "hashtag_name", "parent", "created", "updated", "products","children"]

    def get_products(self, obj):
        products = Product.objects.filter(category=obj)[
            :5
        ]  # Har bir kategoriya uchun 5 mahsulot
        return ProductSerializer(products, many=True).data
    def get_children(self,obj):
        children = Category.objects.filter(parent=obj)
        return CategorySerializer(children, many=True).data
class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "title", "image", "head_name", "hashtag_name", "parent", "created", "updated"]

