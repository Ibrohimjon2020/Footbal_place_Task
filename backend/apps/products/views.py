from apps.categories.models import Category
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, response, status, viewsets

from .filters import ProductFilter
from .models import Banner, Product
from .serializers import (BannerCreateSerializer, BannerSerializer,
                          ProductCreateSerializer, ProductSerializer,
                          ProductSerializerAdmin, ProductSerializerForUrl)


class ProductViewSet(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    queryset = Product.objects.filter(is_active=True).order_by("-id")
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_class = ProductFilter
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
            openapi.Parameter(
                "category",
                openapi.IN_QUERY,
                description="category bo'yicha productslarni qaytarish",
                type=openapi.TYPE_INTEGER,
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
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """
        Custom queryset to handle filtering by category and its children,
        and a parameter to return all products.
        """
        queryset = super().get_queryset()
        category_id = self.request.query_params.get("category", None)
        all_products = self.request.query_params.get("all", None)

        if all_products:
            return queryset  # Return all products if 'all=true' is provided

        if category_id:
            # Get the category and its children's ids
            category = Category.objects.get(pk=category_id)
            child_categories = category.childeren.all()
            child_ids = [category.id for category in child_categories]
            child_ids.append(category.id)  # Include the parent category itself
            print(queryset.filter(category_id__in=child_ids))
            # Filter products belonging to the category and its children
            queryset = queryset.filter(category_id__in=child_ids)

        return queryset

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProductSerializer
        return ProductCreateSerializer


class ProductViewSetAdmin(viewsets.ModelViewSet):
    # queryset = Product.objects.all()
    queryset = Product.objects.filter(is_active=True).order_by("-id")
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_class = ProductFilter
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
            openapi.Parameter(
                "category",
                openapi.IN_QUERY,
                description="category bo'yicha productslarni qaytarish",
                type=openapi.TYPE_INTEGER,
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
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def get_queryset(self):
        """
        Custom queryset to handle filtering by category and its children,
        and a parameter to return all products.
        """
        queryset = super().get_queryset()
        category_id = self.request.query_params.get("category", None)
        all_products = self.request.query_params.get("all", None)

        if all_products:
            return queryset  # Return all products if 'all=true' is provided

        if category_id:
            # Get the category and its children's ids
            category = Category.objects.get(pk=category_id)
            child_categories = category.childeren.all()
            child_ids = [category.id for category in child_categories]
            child_ids.append(category.id)  # Include the parent category itself
            print(queryset.filter(category_id__in=child_ids))
            # Filter products belonging to the category and its children
            queryset = queryset.filter(category_id__in=child_ids)

        return queryset

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProductSerializerAdmin
        return ProductCreateSerializer


class ProductForUrlListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializerForUrl
    pagination_class = None


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.order_by("-id").all()
    # queryset = Banner.objects.filter(is_active=True).order_by('-id')
    serializer_class = BannerSerializer

    def update(self, request, pk, *args, **kwargs):
        instance = self.get_object()
        # print(instance)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        if request.data.get("is_active") == True:
            update = Banner.objects.update(is_active=False)
        self.perform_update(serializer)

        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return BannerSerializer
        return BannerCreateSerializer
