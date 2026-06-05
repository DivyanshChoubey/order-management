from rest_framework import serializers

from service.models import Order
from service.serializers.customer_get_serializer import CustomerGetSerializer
from service.serializers.order_item_get_serializer import \
    OrderItemGetSerializer


class OrderGetSerializer(serializers.ModelSerializer):
    customer = CustomerGetSerializer(read_only=True)
    items = OrderItemGetSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "customer",
            "items",
            "created_at",
            "updated_at",
        ]
