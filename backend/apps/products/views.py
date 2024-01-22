from rest_framework import viewsets
from rest_framework import views
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Banner
from apps.categories.models import Category
from .serializers import ProductSerializer, BannerSerializer
from apps.accounts.permissions import IsAdminOrReadOnly, IsOwnerOrReadonly



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]
    permission_classes = [IsAdminOrReadOnly, IsOwnerOrReadonly]

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
            openapi.Parameter(
                "category",
                openapi.IN_QUERY,
                description="category bo'yicha productslarni qaytarish",
                type=openapi.TYPE_INTEGER,
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        params = self.request.query_params

        if params.get("all") == "true":
            # Barcha mahsulotlarni qaytarish (paginationni o'chirib)
            queryset = Product.objects.all()
            serializer = self.get_serializer(queryset, many=True)
            return views.Response(serializer.data)

        pattern_category = params.get("category")
        if pattern_category:
            try:
                category = Category.objects.get(pk=pattern_category)
                if category.childeren.exists():
                    categories = Category.objects.filter(parent=category)
                    queryset = Product.objects.filter(category__in=categories)
                    # Bu yerda ham pagination qo'llanishi kerak
                    page = self.paginate_queryset(queryset)
                    if page is not None:
                        serializer = self.get_serializer(page, many=True)
                        return self.get_paginated_response(serializer.data)
                    serializer = self.get_serializer(queryset, many=True)
                    return views.Response(serializer.data)
            except Category.DoesNotExist:
                return views.Response(
                    []
                )  # Agar kategoriya topilmasa, bo'sh ro'yxat qaytarish

        # Agar maxsus parametrlar bo'lmasa, standart list metodini ishlatish
        return super().list(request, *args, **kwargs)


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [IsAdminOrReadOnly, IsOwnerOrReadonly]

