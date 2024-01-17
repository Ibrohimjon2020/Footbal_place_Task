from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Banner
from apps.categories.models import Category
from .serializers import ProductSerializer, BannerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "limit",
                openapi.IN_QUERY,
                description="Har bir sahifada qaytariladigan natijalar soni",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                "offset",
                openapi.IN_QUERY,
                description="Natijalarni qaytarishni boshlash indeksi",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                "all",
                openapi.IN_QUERY,
                description="Barcha kategoriyalarni qaytaradi. Qiymati 'true' bo'lsa, pagination qo'llanilmaydi.",
                type=openapi.TYPE_BOOLEAN,
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        # Foydalanuvchidan kelgan so'rovni olish
        params = self.request.query_params
        pattern_category = self.kwargs.get("pk")
        category = Category.objects.get(pk=pattern_category)
        if category.childeren.exists():
            try:
                categories = category.get_descendants(include_self=True)
                return Product.objects.filter(category__in=categories)
            except Category.DoesNotExist:
                # Agar berilgan kategoriya mavjud bo'lmasa, bo'sh queryset qaytarish
                return Product.objects.none()
        # Agar 'all' so'rovi bo'lsa, barcha ob'ektlarni qaytarish
        if params.get("all") == "true":
            return Product.objects.all()
        # Aks holda, standart queryset (pagination bilan)
        else:
            return super().get_queryset()


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
