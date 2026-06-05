from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from service.constants import ResponseMessages
from service.models import Order
from service.serializers import OrderGetSerializer


class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all().order_by("-id")
        serializer = OrderGetSerializer(orders, many=True)

        return Response(
            {
                "success": True,
                "message": ResponseMessages.ORDER_FETCHED,
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
