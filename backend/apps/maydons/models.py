from django.db import models
from django.conf import settings 

# Create your models here.    
class Maydon(models.Model):
    nomi = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    rasmlari = models.ImageField(upload_to='maydonlar/')
    bron_qilish_narxi = models.FloatField()
    uzunlik = models.FloatField()
    enlik = models.FloatField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomi