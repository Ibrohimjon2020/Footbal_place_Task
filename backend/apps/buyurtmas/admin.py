from django.contrib import admin
from django.utils.html import format_html

from .models import Buyurtma

class BuyurtmaAdmin(admin.ModelAdmin):
    list_display = ('maydon_id','narxi','user_id','sana','soat_dan','soat_gacha','created_at','updated_at')


admin.site.register(Buyurtma, BuyurtmaAdmin)
