from django.urls import path
from service.views import *


urlpatterns =[
    path("customer/create", CustomerCreateView.as_view(), name="customer-create"),
    path("customer/update", CustomerUpdateView.as_view(), name="customer-update"),
    path("product/create", ProductCreateView.as_view(), name="product-create"),
    path("product/update", ProductUpdateView.as_view(), name="product-update"),
    path("order/create", OrderCreateView.as_view(), name="order-create"),
    path("order/update", OrderUpdateView.as_view(), name="order-update"),
    path("order/list", OrderListView.as_view(), name="order-list"),
]
