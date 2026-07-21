from django.urls import path
from . import views

urlpatterns = [

    path(
        "add-to-cart/<int:id>/",
        views.add_to_cart,
        name="add_to_cart"
    ),
    path(
    "view-cart/",
    views.view_cart,
    name="view_cart"
),

    path(
    "increase/<int:id>/",
    views.increase_quantity,
    name="increase_quantity"
),

path(
    "decrease/<int:id>/",
    views.decrease_quantity,
    name="decrease_quantity"
),

path(
    "remove/<int:id>/",
    views.remove_cart,
    name="remove_cart"
),



]