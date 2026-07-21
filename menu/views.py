from django.shortcuts import render, redirect, get_object_or_404
from .forms import FoodMenuForm
from .models import FoodMenu
from accounts.models import VendorDetails
from django.contrib.auth.decorators import login_required

# CREATE

@login_required(login_url="login")
def menubuilding(request):

    vendor = get_object_or_404(VendorDetails, user=request.user)

    if request.method == "POST":
        form = FoodMenuForm(request.POST, request.FILES)

        if form.is_valid():

            food = form.save(commit=False)
            food.restaurant = vendor
            food.save()

            return redirect("foodlist")

    else:
        form = FoodMenuForm()

    return render(request, "accounts/menubuilding.html", {"form": form})

# READ

@login_required(login_url="login")
def foodlist(request):

    vendor = get_object_or_404(VendorDetails, user=request.user)

    foods = FoodMenu.objects.filter(restaurant=vendor)

    return render(request, "accounts/foodlist.html", {
        "foods": foods
    })

# UPDATE
@login_required(login_url="login")
def updatefood(request, id):

    vendor = get_object_or_404(VendorDetails, user=request.user)

    food = get_object_or_404(
        FoodMenu,
        id=id,
        restaurant=vendor
    )

    if request.method == "POST":
        form = FoodMenuForm(request.POST, request.FILES, instance=food)

        if form.is_valid():
            form.save()
            return redirect("foodlist")

    else:
        form = FoodMenuForm(instance=food)

    return render(request, "accounts/updatefood.html", {
        "form": form
    })

# DELETE
@login_required(login_url="login")
def deletefood(request, id):

    vendor = get_object_or_404(VendorDetails, user=request.user)

    food = get_object_or_404(
        FoodMenu,
        id=id,
        restaurant=vendor
    )

    food.delete()

    return redirect("foodlist")


from django.shortcuts import render, get_object_or_404
from .models import FoodMenu
from django.db.models import Avg

def food_details(request, id):

    food = get_object_or_404(
        FoodMenu.objects.annotate(
            average_rating=Avg("review__rating")
        ),
        id=id
    )

    return render(
        request,
        "accounts/food_details.html",
        {
            "food": food
        }
    )
