from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name




