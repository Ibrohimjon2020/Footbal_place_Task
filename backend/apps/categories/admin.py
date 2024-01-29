from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Category

# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'parent', 'description', 'title', 'head_name') 

# admin.site.register(Category, CategoryAdmin)

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'parent', 'description', 'title', 'order', 'head_name', 'hashtag_name')
