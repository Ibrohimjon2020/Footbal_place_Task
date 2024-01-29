from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Banner, Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'price', 'description', 'category', 'prepare_time')

@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    list_display = ('title', 'summary', 'body')

