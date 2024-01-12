from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        # Foydalanuvchidan kelgan so'rovni olish
        params = self.request.query_params

        # Agar 'all' so'rovi bo'lsa, barcha ob'ektlarni qaytarish
        if params.get("all") == "true":
            return Product.objects.all()
        # Aks holda, standart queryset (pagination bilan)
        else:
            return super().get_queryset()
