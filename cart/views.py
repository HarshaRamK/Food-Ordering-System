
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart
from menu.models import FoodMenu

@login_required
def add_to_cart(request, id):

    food = get_object_or_404(FoodMenu, id=id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        food=food
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("view_cart")

from .models import Cart

@login_required
def view_cart(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        total += item.food.price * item.quantity

    return render(request, "accounts/view_cart.html", {
        "cart_items": cart_items,
        "total": total
    })

from django.shortcuts import get_object_or_404

@login_required
def increase_quantity(request, id):

    cart_item = get_object_or_404(
        Cart,
        id=id,
        user=request.user
    )

    cart_item.quantity += 1
    cart_item.save()

    return redirect("view_cart")


@login_required
def decrease_quantity(request, id):

    cart_item = get_object_or_404(
        Cart,
        id=id,
        user=request.user
    )

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect("view_cart")

@login_required
def remove_cart(request, id):

    cart_item = get_object_or_404(
        Cart,
        id=id,
        user=request.user
    )

    cart_item.delete()

    return redirect("view_cart")

