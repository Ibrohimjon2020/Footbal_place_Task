# Generated by Django 4.2.8 on 2024-01-16 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_category_description_category_image_category_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='hashtag_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='head_name',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
