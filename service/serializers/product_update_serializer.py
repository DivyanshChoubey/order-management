from rest_framework import serializers


class ProductUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
