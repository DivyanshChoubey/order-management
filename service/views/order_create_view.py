from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from service.serializers import OrderCreateSerializer
from service.models import Customer, Product, Order, OrderItem
from service.constants import ResponseMessages


class OrderCreateView(APIView):
    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)
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
            customer = Customer.objects.get(id=data["customer_id"])
        except Customer.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": ResponseMessages.CUSTOMER_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )

        order = Order.objects.create(customer=customer)

        for item_data in data.get("items", []):
            try:
                product = Product.objects.get(id=item_data["product_id"])
            except Product.DoesNotExist:
                order.delete()
                return Response(
                    {
                        "success": False,
                        "message": ResponseMessages.PRODUCT_NOT_FOUND
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item_data["quantity"]
            )

        return Response(
            {
                "success": True,
                "message": ResponseMessages.ORDER_CREATED
            },
            status=status.HTTP_201_CREATED
        )
