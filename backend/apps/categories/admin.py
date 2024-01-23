from django.contrib import admin

from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'description', 'title', 'head_name') 

admin.site.register(Category, CategoryAdmin)
