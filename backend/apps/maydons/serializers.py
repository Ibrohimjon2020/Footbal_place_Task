import json
from django.conf import settings
from rest_framework import serializers
from .models import Maydon

class MaydonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maydon
        fields = '__all__'