from django.urls import path
from . import views

urlpatterns = [

    path(
        "payment/<int:order_id>/",
        views.payment_page,
        name="payment"
    ),

    path(
        "success/",
        views.order_success,
        name="order_success"
    ),

]