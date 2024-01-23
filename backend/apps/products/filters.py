from apps.categories.models import Category
from django_filters import rest_framework as filters

from .models import Product


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ["category"]

    @property
    def qs(self):
        parent = super().qs
        print(parent, "bosh")
        params = self.request.query_params
        all_products = params.get("all") == "true"
        pattern_category = params.get("category")

        if all_products:
            return Product.objects.all()

        if pattern_category:
            try:
                category = Category.objects.get(pk=pattern_category)
                if category.childeren.exists():
                    categories = Category.objects.filter(parent=category)
                    print(categories, "cat")
                    print(parent, "par")
                    print(parent.filter(category__in=categories))
                    return parent.filter(category__in=categories)
            except Category.DoesNotExist:
                return Product.objects.none()

        return parent
