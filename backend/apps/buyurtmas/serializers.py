import json
from django.conf import settings
from rest_framework import serializers
from .models import Buyurtma

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'