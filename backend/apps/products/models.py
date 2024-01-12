from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.ImageField(upload_to="product/image/", null=True)
    gif = models.FileField(upload_to="product/gif/", null=True)
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    prepare_time = models.PositiveIntegerField(blank=True, default=0)
    category = models.ForeignKey(to="categories.Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
