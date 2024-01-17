from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='category_images', blank=True)
    head_name = models.CharField(max_length=100, null=True, blank=True)
    hashtag_name = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name




