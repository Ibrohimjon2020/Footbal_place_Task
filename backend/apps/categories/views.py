from django.shortcuts import render
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        # Foydalanuvchidan kelgan so'rovni olish
        params = self.request.query_params

        # Agar 'all' so'rovi bo'lsa, barcha ob'ektlarni qaytarish
        if params.get("all") == "true":
            return Category.objects.all()
        # Aks holda, standart queryset (pagination bilan)
        else:
            return super().get_queryset()
