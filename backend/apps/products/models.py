from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.ImageField(upload_to="product/image/", null=True, blank=True)
    gif = models.FileField(
        upload_to="product/gif/",
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["gif", "mp4", "mov"]),
        ],
    )
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    prepare_time = models.PositiveIntegerField(blank=True, default=0)
    category = models.ForeignKey(
        to="categories.Category",
        on_delete=models.CASCADE,
        related_name="cat_products",
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"


class Banner(models.Model):
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/banner", blank=True)
    video = models.FileField(upload_to="banners/video", null=True)
    body = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
