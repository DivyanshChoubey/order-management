__all__ = [
    "CustomerCreateView",
    "CustomerUpdateView",
    "ProductCreateView",
    "ProductUpdateView",
    "OrderCreateView",
    "OrderUpdateView",
    "OrderListView",
]

from service.views.customer_create_view import CustomerCreateView
from service.views.customer_update_view import CustomerUpdateView
from service.views.product_create_view import ProductCreateView
from service.views.product_update_view import ProductUpdateView
from service.views.order_create_view import OrderCreateView
from service.views.order_update_view import OrderUpdateView
from service.views.order_list_view import OrderListView
