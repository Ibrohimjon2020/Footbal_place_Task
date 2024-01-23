from django.contrib import admin

from .models import Banner, Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category', 'prepare_time')


admin.site.register(Product, ProductAdmin)
admin.site.register(Banner)
