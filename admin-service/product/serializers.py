from rest_framework import serializers
from product import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"
        extra_kwargs = {
            'title': {'required': False},
            'image': {'required': False}
        }