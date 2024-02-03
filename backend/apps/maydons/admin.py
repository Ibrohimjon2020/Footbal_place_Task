from django.contrib import admin
from django.utils.html import format_html

from .models import Maydon

class MaydonAdmin(admin.ModelAdmin):
    list_display = ('nomi','address', 'contact', 'rasmlari', 'bron_qilish_narxi') 
admin.site.register(Maydon, MaydonAdmin)