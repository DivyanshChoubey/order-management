from rest_framework import serializers


class OrderItemUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    product_id = serializers.IntegerField(required=False)
    quantity = serializers.IntegerField(min_value=1, required=False)
