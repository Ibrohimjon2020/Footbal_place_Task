from django.db import models
from django.conf import settings 

# Create your models here.    
class Buyurtma(models.Model):
    maydon_id = models.ForeignKey('maydons.Maydon', on_delete=models.CASCADE)
    narxi = models.FloatField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    sana = models.DateField()
    soat_dan = models.TimeField()
    soat_gacha = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    