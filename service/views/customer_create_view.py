from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from service.constants import ResponseMessages
from service.models import Customer
from service.serializers import CustomerCreateSerializer


class CustomerCreateView(APIView):
    def post(self, request):
        serializer = CustomerCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "message": ResponseMessages.INVALID_DATA,
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        data = serializer.validated_data

        Customer.objects.create(
            name=data["name"],
            email=data["email"]
        )

        return Response(
            {
                "success": True,
                "message": ResponseMessages.CUSTOMER_CREATED
            },
            status=status.HTTP_201_CREATED
        )
