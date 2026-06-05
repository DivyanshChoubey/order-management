from rest_framework import serializers

from service.models import Customer


class CustomerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "name",
            "email",
            "created_at",
            "updated_at",
        ]
