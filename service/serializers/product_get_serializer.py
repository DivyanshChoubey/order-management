from rest_framework import serializers

from service.models import Product


class ProductGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "created_at",
            "updated_at",
        ]
