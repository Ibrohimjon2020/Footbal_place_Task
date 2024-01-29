from django.contrib import admin
from django.utils.html import format_html

from .models import Category

from modeltranslation.admin import TranslationAdmin


# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'parent', 'description', 'title', 'head_name') 

# admin.site.register(Category, CategoryAdmin)

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('image_tag', 'name', 'parent', 'description', 'title', 'order',)

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 80px; width: 200px; object-fit: contain;" />'.format(obj.image.url))
        else:
            return None
