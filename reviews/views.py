from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from menu.models import FoodMenu
from orders.models import Order
from .models import Review


@login_required
def add_review(request, id):

    food = get_object_or_404(FoodMenu, id=id)

    delivered = Order.objects.filter(
        user=request.user,
        food=food,
        status="Delivered"
    ).exists()

    if not delivered:
        return redirect("my_orders")

    if request.method == "POST":

        rating = request.POST.get("rating")
        review = request.POST.get("review")

        Review.objects.update_or_create(
            user=request.user,
            food=food,
            defaults={
                "rating": rating,
                "review": review,
            }
        )

        return redirect("view_restaurant", id=food.restaurant.id)

    return render(request, "accounts/review_form.html", {
        "food": food
    })