import sys

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, views, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Category
from .serializers import CategoryCreateSerializer, CategorySerializer, CategoryParentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    # queryset = Category.objects.prefetch_related("cat_products").all()
    queryset = Category.objects.prefetch_related("cat_products").order_by('order', '-id').all()

    # serializer_class = CategorySerializer

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
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return views.Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queryset = super().get_queryset()
        all_products = self.request.query_params.get("all", None)

        if all_products:
            return queryset
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CategorySerializer
        if self.action == 'get_parent_categories':
            return CategoryParentSerializer
        return CategoryCreateSerializer

    @action(detail=False, methods=['get'])
    def get_parent_categories(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset().filter(parent__isnull=True)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return views.Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            trace_back = sys.exc_info()[2]
            line = trace_back.tb_lineno
            res = {'msg': str(e) + ' --- line -' + str(line)}
            return Response(res, status=400)
