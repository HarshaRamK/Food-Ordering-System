from django.urls import path
from . import views

urlpatterns = [

    path(
        "checkout/",
        views.checkout,
        name="checkout"
    ),
    path("my-orders/", views.my_orders, name="my_orders"),
    path(
    "place-order/",
    views.place_order,
    name="place_order"
),
path(
    "vendor-orders/",
    views.vendor_orders,
    name="vendor_orders"
),
path(
    "update-status/<int:id>/",
    views.update_order_status,
    name="update_order_status"
),
path(
    "update-status/<int:id>/<str:status>/",
    views.update_order_status,
    name="update_order_status",
),

path(
    "cancel/<int:id>/",
    views.cancel_order,
    name="cancel_order",
),
]