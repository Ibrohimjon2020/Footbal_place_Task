# Generated by Django 4.2.8 on 2024-02-02 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maydons', '0003_maydon_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narxi', models.FloatField()),
                ('sana', models.DateField()),
                ('soat_dan', models.TimeField()),
                ('soat_gacha', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('maydon_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maydons.maydon')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
