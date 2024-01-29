# Generated by Django 4.2.8 on 2024-01-25 11:56

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0010_alter_category_image_alter_category_name'),
        ('products', '0013_alter_product_gif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat_products', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='gif',
            field=models.FileField(blank=True, null=True, upload_to='product/gif/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['gif', 'mp4', 'mov'])]),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/image/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
