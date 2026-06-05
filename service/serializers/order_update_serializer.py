from rest_framework import serializers

from service.serializers.order_item_update_serializer import \
    OrderItemUpdateSerializer


class OrderUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    customer_id = serializers.IntegerField(required=False)
    items = OrderItemUpdateSerializer(many=True, required=False)
