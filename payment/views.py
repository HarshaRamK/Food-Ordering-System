

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order
from .models import Payment
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def payment_page(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    if request.method == "POST":

        method = request.POST.get("payment_method")

        Payment.objects.create(
            order=order,
            user=request.user,
            payment_method=method,
            amount=order.total_price,
            payment_status="Success"
        )

        return redirect("order_success")

    return render(request, "payment/payment.html", {
        "order": order
    })


@login_required(login_url="login")
def order_success(request):
    return render(request, "payment/order_success.html")