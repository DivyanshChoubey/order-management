from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from service.constants import ResponseMessages
from service.models import Customer
from service.serializers import CustomerUpdateSerializer


class CustomerUpdateView(APIView):
    def patch(self, request):
        serializer = CustomerUpdateSerializer(data=request.data)
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

        try:
            customer = Customer.objects.get(id=data["id"])
        except Customer.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": ResponseMessages.CUSTOMER_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if "name" in data:
            customer.name = data["name"]
        if "email" in data:
            customer.email = data["email"]
        customer.save()

        return Response(
            {
                "success": True,
                "message": ResponseMessages.CUSTOMER_UPDATED
            },
            status=status.HTTP_200_OK
        )
