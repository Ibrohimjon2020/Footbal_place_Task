from django.db import models
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10,decimal_places=3)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    prepare_time = models.PositiveIntegerField(blank=True)
    category = models.ForeignKey(to='categories.Category', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    


class ProductGallery(models.Model):
    media = models.FileField(upload_to='product')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product.name
