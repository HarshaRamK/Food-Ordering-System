from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from menu.models import FoodMenu
from .models import Wishlist


@login_required
def add_to_wishlist(request, id):

    food = get_object_or_404(FoodMenu, id=id)

    Wishlist.objects.get_or_create(
        user=request.user,
        food=food
    )

    return redirect("view_restaurant", id=food.restaurant.id)


@login_required
def view_wishlist(request):

    wishlist_items = Wishlist.objects.filter(user=request.user)

    return render(request, "accounts/wishlist.html", {
        "wishlist_items": wishlist_items
    })


@login_required
def remove_wishlist(request, id):

    item = get_object_or_404(
        Wishlist,
        id=id,
        user=request.user
    )

    item.delete()

    return redirect("view_wishlist")