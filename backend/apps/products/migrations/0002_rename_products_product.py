# Generated by Django 4.2.8 on 2024-01-11 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_rename_categorys_category'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
