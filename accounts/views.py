#views.py handles the business logic of entire project
from django.shortcuts import render,redirect
from accounts.forms import UserForm,UserProfileForm,UserUpdateForm,ProfileUpdateForm,VendorForm,VendorProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from reviews.models import Review

# Create your views here.
def registration(request):
    registered = False
    if request.method == 'POST':
        form1 = UserForm(request.POST)
        form2=UserProfileForm(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()

            profile = form2.save(commit=False)
            profile.user = user     #merging two forms
            profile.save()
            registered = True
    else:     
        form1 = UserForm()
        form2 = UserProfileForm()
   
    context ={
              'form1':form1,
              'form2':form2,
              'registered':registered,
              }
    return render(request,"accounts/resgistration.html",context)


from accounts.models import VendorDetails

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

                try:
                    vendor = user.vendordetails

                    if vendor.is_approved:
                        return redirect('vendor_dashboard')  # ✅ approved vendor
                    else:
                        return redirect('approved')  # ⛔ not approved

                except VendorDetails.DoesNotExist:
                    return redirect('home')  # 👤 normal user

        else:
            return HttpResponse("Invalid credentials")

    return render(request, "accounts/login.html")



from accounts.forms import VendorProfileUpdateForm
@login_required
def vendor_update(request):

    vendor = request.user.vendordetails

    if request.method == "POST":

        form = VendorProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=vendor
        )

        if form.is_valid():
            form.save()
            print("Saved Successfully")
            return redirect("vendor_profile")
        else:
            print(form.errors)

    else:
        form = VendorProfileUpdateForm(instance=vendor)

    return render(
        request,
        "accounts/vendor_update.html",
        {"form": form}
    )

from django.contrib.auth.decorators import login_required


@login_required
def vendor_profile(request):
    return render(request, "accounts/vendor_profile.html")


# @login_required
# def vendor_orders(request):
#     return render(request, "accounts/vendor_orders.html")



from django.db.models import Q
from accounts.models import VendorDetails
from menu.models import FoodMenu

def home(request):

    search = request.GET.get("search")

    # If user is logged in, get user's zipcode
    if request.user.is_authenticated:
        user_zip = str(request.user.userdetails.zipcode)

        # Get the first 3 digits
        zip_prefix = user_zip[:3]

        restaurants = VendorDetails.objects.filter(
            zipcode__startswith=zip_prefix,
            is_approved=True
        )

        foods = FoodMenu.objects.filter(
            restaurant__zipcode__startswith=zip_prefix
        )

    else:
        # Guest users
        restaurants = VendorDetails.objects.filter(
            is_approved=True
        )[:3]

        foods = FoodMenu.objects.order_by("?")[:6]

    # Search
    if search:

        restaurants = restaurants.filter(
            Q(RestaurentName__icontains=search) |
            Q(Restaurent_address__icontains=search)
        )

        foods = foods.filter(
            Q(foodname__icontains=search) |
            Q(description__icontains=search)
        )

    else:
        # Show only 3 restaurants and 6 random foods
        restaurants = restaurants[:3]
        foods = foods.order_by("?")[:6]

    return render(request, "home.html", {
        "restaurants": restaurants,
        "foods": foods,
    })

from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import VendorDetails
from menu.models import FoodMenu
from reviews.models import Review



def view_restaurant(request, id):

    restaurant = get_object_or_404(
        VendorDetails,
        id=id
    )

    foods = FoodMenu.objects.filter(
    restaurant=restaurant
    ).annotate(
        average_rating=Avg("review__rating")
    )

    search = request.GET.get("search")
    food_type = request.GET.get("type")

    if search:
        foods = foods.filter(
            foodname__icontains=search
        )

    if food_type:
        foods = foods.filter(
            type=food_type
        )

    reviews = Review.objects.filter(
        food__restaurant=restaurant
    ).order_by("-review_date")

    average_rating = reviews.aggregate(
        Avg("rating")
    )["rating__avg"]

    return render(
        request,
        "accounts/restaurant_details.html",
        {
            "restaurant": restaurant,
            "foods": foods,
            "reviews": reviews,
            "average_rating": average_rating,
        }
    )

from django.contrib.auth.decorators import login_required
from accounts.models import VendorDetails
from menu.models import FoodMenu
from orders.models import Order

@login_required(login_url="login")
def vendor_dashboard(request):

    restaurant = VendorDetails.objects.get(user=request.user)

    total_foods = FoodMenu.objects.filter(
        restaurant=restaurant
    ).count()

    pending_orders = Order.objects.filter(
        food__restaurant=restaurant,
        status="Pending"
    ).count()

    completed_orders = Order.objects.filter(
        food__restaurant=restaurant,
        status="Delivered"
    ).count()

    return render(request, "accounts/vendor_dashboard.html", {
        "total_foods": total_foods,
        "pending_orders": pending_orders,
        "completed_orders": completed_orders,
    })


from django.db.models import Q
from django.contrib.auth.decorators import login_required
from accounts.models import VendorDetails

@login_required
def restaurants(request):

    user_zip = str(request.user.userdetails.zipcode)
    zip_prefix = user_zip[:3]

    search = request.GET.get("search")

    restaurants = VendorDetails.objects.filter(
        zipcode__startswith=zip_prefix,
        is_approved=True
    )

    if search:
        restaurants = restaurants.filter(
            Q(RestaurentName__icontains=search) |
            Q(Restaurent_address__icontains=search)
        )

    return render(request, "accounts/restaurants.html", {
        "restaurants": restaurants
    })

# def vendorregistration(request):
#     registered = False

#     if request.method == 'POST':
#         form1 = VendorForm(request.POST)
#         form2 = VendorProfileForm(request.POST, request.FILES)

#         if form1.is_valid() and form2.is_valid():
#             user = form1.save()
#             user.set_password(user.password)
#             user.save()

#             profile = form2.save(commit=False)
#             profile.user = user
#             profile.save()

#             registered = True
#     else:
#         form1 = VendorForm()
#         form2 = VendorProfileForm()

#     return render(request, "accounts/vendorreg.html", {
#         'form1': form1,
#         'form2': form2,
#         'registered': registered
#     })

# def vendorregistration(request):
#     registered = False

#     if request.method == 'POST':
#         form1 = VendorForm(request.POST)
#         form2 = VendorProfileForm(request.POST, request.FILES)

#         if form1.is_valid() and form2.is_valid():
#             print("✅ Forms are valid")

#             user = form1.save()
#             user.set_password(user.password)
#             user.save()

#             profile = form2.save(commit=False)
#             profile.user = user
#             profile.save()

#             registered = True
#         else:
#             print("❌ Form1 Errors:", form1.errors)
#             print("❌ Form2 Errors:", form2.errors)

#     else:
#         form1 = VendorForm()
#         form2 = VendorProfileForm()

#     return render(request, "accounts/vendorreg.html", {
#         'form1': form1,
#         'form2': form2,
#         'registered': registered
#     })


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username=username,password=password)

#         if user:
#             if user.is_active:
#                 login(request,user)
#                 return redirect('home')
#         else:
#             return HttpResponse("Please check your creds...!")
#     return render(request,"accounts/login.html")

def vendorregistration(request):
    registered = False

    if request.method == 'POST':
        form1 = VendorForm(request.POST)
        form2 = VendorProfileForm(request.POST, request.FILES)

        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()

            profile = form2.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
    else:
        form1 = VendorForm()
        form2 = VendorProfileForm()

    return render(request, "accounts/vendorreg.html", {
        'form1': form1,
        'form2': form2,
        'registered': registered
    })


@login_required(login_url="login")
def user_logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def profile(request):
    return render(request,'accounts/profile.html',{})

@login_required(login_url="login")
def update(request):
    if request.method=='POST':
        form=UserUpdateForm(request.POST,instance=request.user)
        form1=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userdetails)
        if form.is_valid():
            user=form.save()
            user.save()

            profile=form1.save()
            profile.user=user
            profile.save()
            return redirect('profile')
    else:
        form=UserUpdateForm(instance=request.user)
        form1=ProfileUpdateForm(instance=request.user.userdetails)

    return render(request,'accounts/update.html',{'form':form,'form1':form1})

# @login_required(login_url="login")
# def vendor_dashboard(request):
#     return render(request, "accounts/dashboard.html")

from django.contrib.auth.decorators import login_required



@login_required(login_url="login")
def approved(request):
    return render(request, "accounts/approved.html")



from accounts.models import VendorDetails

from accounts.models import VendorDetails

