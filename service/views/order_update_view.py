from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from service.serializers import OrderUpdateSerializer
from service.models import Customer, Product, Order, OrderItem
from service.constants import ResponseMessages


class OrderUpdateView(APIView):
    def patch(self, request):
        serializer = OrderUpdateSerializer(data=request.data)
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
            order = Order.objects.get(id=data["id"])
        except Order.DoesNotExist:
            return Response(
                {
                    "success": False,
                    "message": ResponseMessages.ORDER_NOT_FOUND
                },
                status=status.HTTP_404_NOT_FOUND
            )

        if "customer_id" in data:
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
            order.customer = customer
        order.save()

        if "items" in data:
            for item_data in data["items"]:
                try:
                    order_item = OrderItem.objects.get(id=item_data["id"], order=order)
                except OrderItem.DoesNotExist:
                    return Response(
                        {
                            "success": False,
                            "message": ResponseMessages.ORDER_ITEM_NOT_FOUND
                        },
                        status=status.HTTP_404_NOT_FOUND
                    )
                if "product_id" in item_data:
                    try:
                        product = Product.objects.get(id=item_data["product_id"])
                    except Product.DoesNotExist:
                        return Response(
                            {
                                "success": False,
                                "message": ResponseMessages.PRODUCT_NOT_FOUND
                            },
                            status=status.HTTP_404_NOT_FOUND
                        )
                    order_item.product = product
                if "quantity" in item_data:
                    order_item.quantity = item_data["quantity"]
                order_item.save()

        return Response(
            {
                "success": True,
                "message": ResponseMessages.ORDER_UPDATED
            },
            status=status.HTTP_200_OK
        )
