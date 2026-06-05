from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from service.constants import ResponseMessages
from service.models import Product
from service.serializers import ProductCreateSerializer


class ProductCreateView(APIView):
    def post(self, request):
        serializer = ProductCreateSerializer(data=request.data)
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

        Product.objects.create(
            name=data["name"],
            price=data["price"]
        )

        return Response(
            {
                "success": True,
                "message": ResponseMessages.PRODUCT_CREATED
            },
            status=status.HTTP_201_CREATED
        )
