
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from .models import Order
from django.shortcuts import redirect


@login_required
def checkout(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.food.price * item.quantity

    return render(request, "accounts/checkout.html", {
        "cart_items": cart_items,
        "total": total
    })


@login_required
def my_orders(request):

    orders = Order.objects.filter(user=request.user).order_by('-order_date')

    return render(request, "accounts/my_orders.html", {
        "orders": orders
    })



from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from cart.models import Cart
from .models import Order

@login_required
def place_order(request):

    cart_items = Cart.objects.filter(user=request.user)

    for item in cart_items:

        Order.objects.create(
            user=request.user,
            food=item.food,
            quantity=item.quantity,
            total_price=item.food.price * item.quantity,
            status="Pending",
            payment_method="Cash on Delivery",
            payment_status="Pending",
        )

    cart_items.delete()

    return redirect("my_orders")

from accounts.models import VendorDetails
from django.contrib.auth.decorators import login_required

@login_required
def vendor_orders(request):

    restaurant = VendorDetails.objects.get(user=request.user)

    orders = Order.objects.filter(
        food__restaurant=restaurant
    ).order_by("-order_date")

    return render(request, "accounts/vendor_orders.html", {
        "orders": orders
    })


from django.shortcuts import get_object_or_404, redirect
from .models import Order

from django.shortcuts import get_object_or_404, redirect
from .models import Order

@login_required(login_url="login")
def update_order_status(request, id, status):

    order = get_object_or_404(Order, id=id)

    order.status = status

    # Automatically update payment status
    if status == "Delivered":
        order.payment_status = "Paid"

    order.save()

    return redirect("vendor_orders")


@login_required
def cancel_order(request, id):

    order = get_object_or_404(
        Order,
        id=id,
        user=request.user
    )

    if order.status == "Pending":
        order.status = "Cancelled"
        order.save()

    return redirect("my_orders")