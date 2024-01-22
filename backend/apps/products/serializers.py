from rest_framework import serializers
from .models import Product, Banner
from django.conf import settings
from apps.accounts.permissions import IsOwnerOrReadonly


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.image and hasattr(instance.image, "url"):
            domain_name = settings.DOMAIN_NAME
            full_path = domain_name + instance.image.url
            representation["image"] = full_path
        else:
            representation["image"] = None

        return representation
    
    def validate(self, data):
        request = self.context['request']
        instance = self.instance
        
        # Permission check using IsOwnerOrReadonly
        if instance and not IsOwnerOrReadonly().has_object_permission(request, None, instance):
            raise serializers.ValidationError("You don't have permission to modify this object.")

        return data


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
    
    def validate(self, data):
        request = self.context['request']
        instance = self.instance
        
        # Permission check using IsOwnerOrReadonly
        if instance and not IsOwnerOrReadonly().has_object_permission(request, None, instance):
            raise serializers.ValidationError("You don't have permission to modify this object.")

        return data
