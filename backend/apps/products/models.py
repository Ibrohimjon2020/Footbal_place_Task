from django.db import models
from apps.categories.models import Categorys
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10,decimal_places=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categorys, on_delete=models.CASCADE)
    
    


class ProductGallery(models.Model):
    media = models.FileField(upload_to='media')
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)