from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class Product(models.Model):
    image = models.ImageField(upload_to="product/image/", null=True)
    gif = models.FileField(upload_to="product/gif/", 
                           null=True, 
                           validators=[
                               FileExtensionValidator(allowed_extensions=['gif', 'mp4', 'mov']),
                                      ]
                           )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    prepare_time = models.PositiveIntegerField(blank=True, default=0)
    category = models.ForeignKey(to="categories.Category", on_delete=models.CASCADE,related_name="cat_products")
    is_active = models.BooleanField(default=True)
        
    def __str__(self):
        return self.name

class Banner(models.Model):
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/banner')
    video = models.FileField(upload_to='banners/video', null=True)
    body = models.TextField()
    is_active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.title
    




