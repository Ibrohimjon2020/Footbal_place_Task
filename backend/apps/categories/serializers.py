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


# CategorySerializer-ni yangilash
class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["id", "name", "created", "updated", "products"]

    def get_products(self, obj):
        products = Product.objects.filter(category=obj)[
            :5
        ]  # Har bir kategoriya uchun 5 mahsulot
        return ProductSerializer(products, many=True).data
