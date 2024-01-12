from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('limit', openapi.IN_QUERY, description="Har bir sahifada qaytariladigan natijalar soni", type=openapi.TYPE_INTEGER),
        openapi.Parameter('offset', openapi.IN_QUERY, description="Natijalarni qaytarishni boshlash indeksi", type=openapi.TYPE_INTEGER),
        openapi.Parameter('all', openapi.IN_QUERY, description="Barcha kategoriyalarni qaytaradi. Qiymati 'true' bo'lsa, pagination qo'llanilmaydi.", type=openapi.TYPE_BOOLEAN),
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        params = self.request.query_params
        if params.get("all") == "true":
            return Category.objects.all()
        else:
            return super().get_queryset()