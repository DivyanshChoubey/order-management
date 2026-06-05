from rest_framework import serializers
from service.models import OrderItem
from service.serializers.product_get_serializer import ProductGetSerializer


class OrderItemGetSerializer(serializers.ModelSerializer):
    product = ProductGetSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product",
            "quantity",
        ]
