from rest_framework import serializers


class CustomerUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, required=False)
    email = serializers.EmailField(required=False)
