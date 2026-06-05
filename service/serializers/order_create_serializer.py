from rest_framework import serializers

from service.serializers.order_item_create_serializer import \
    OrderItemCreateSerializer


class OrderCreateSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    items = OrderItemCreateSerializer(many=True)
