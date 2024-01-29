from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=225, blank=True, null=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="childeren",
    )
    description = models.TextField(blank=True)
    title = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(upload_to="category_images", blank=True, null=True)
    head_name = models.CharField(max_length=100, null=True, blank=True)
    hashtag_name = models.CharField(max_length=100, null=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_descendants(self, include_self=True):
        """
        Bu funksiya berilgan kategoriyaning barcha bolalarini (va kerak bo'lsa o'zini ham)
        rekursiv tarzda qaytaradi.
        """
        descendants = []
        if include_self:
            descendants.append(self)
        for child in Category.objects.filter(parent=self):
            descendants.extend(child.get_descendants(include_self=True))
        return descendants

    def __str__(self):
        return f"{self.name}"
