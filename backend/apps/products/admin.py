from django.contrib import admin
from django.utils.html import format_html

from .models import Banner, Product

from modeltranslation.admin import TranslationAdmin


# Register your models here.

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('image_tag', 'gif_tag', 'name', 'price', 'description', 'category', 'prepare_time')

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 80px; width: 200px; object-fit: contain;" />'.format(obj.image.url))
        else:
            return None
    def gif_tag(self, obj):
        if obj.gif:
            return format_html(
                '<video src="{}" style="max-height: 80px; width: 200px; object-fit: contain;" />'.format(obj.gif.url))
        else:
            return None


@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    list_display = ('image_tag', 'title', 'summary', )

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 80px; width: 200px; object-fit: contain;" />'.format(obj.image.url))
        else:
            return None
