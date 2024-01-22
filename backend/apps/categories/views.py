from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import viewsets, views
from .models import Category
from .serializers import CategorySerializer, CategoryCreateSerializer
from apps.accounts.permissions import IsAdminOrReadOnly, IsOwnerOrReadonly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.prefetch_related("cat_products").all()
    # serializer_class = CategorySerializer
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
        ]
    )
    def list(self, request, *args, **kwargs):
        params = self.request.query_params
        if params.get("all") == "true":
            # Barcha mahsulotlarni qaytarish (paginationni o'chirib)
            queryset = Category.objects.all()
            serializer = self.get_serializer(queryset, many=True)
            return views.Response(serializer.data)
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CategorySerializer
        return CategoryCreateSerializer
