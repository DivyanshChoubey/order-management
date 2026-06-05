from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from service.serializers import ProductUpdateSerializer
from service.models import Product
from service.constants import ResponseMessages


class ProductUpdateView(APIView):
    def patch(self, request):
        serializer = ProductUpdateSerializer(data=request.data)
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
            product = Product.objects.get(id=data["id"])
        except Product.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": ResponseMessages.PRODUCT_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if "name" in data:
            product.name = data["name"]
        if "price" in data:
            product.price = data["price"]
        product.save()

        return Response(
            {
                "success": True,
                "message": ResponseMessages.PRODUCT_UPDATED
            },
            status=status.HTTP_200_OK
        )
