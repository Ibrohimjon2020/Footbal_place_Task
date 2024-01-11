from django.db import models

# Create your models here.

class Categorys(models.Model):
    name = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)




