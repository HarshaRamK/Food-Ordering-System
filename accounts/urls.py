#It handle url configuration of each html page for function call
from django.urls import path
from accounts import views

urlpatterns =[
    path('',views.registration,name='register'),
    path('login',views.user_login,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.user_logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('update',views.update,name='update'),
    # path('vendorlogin',views.vendorregistration,name='vendorregister'),
    # path('vendor_dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('vendor-register/', views.vendorregistration, name='vendorregister'),
    path('vendor-dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('approved/', views.approved, name='approved'),
    path("vendor-profile/",views.vendor_profile,name="vendor_profile"),
    # path("vendor-orders/",views.vendor_orders,name="vendor_orders"),
    path('restaurant/<int:id>/',views.view_restaurant,name='view_restaurant'),
    path("restaurants/", views.restaurants, name="restaurants"),
    path(
    "vendor-update/",
    views.vendor_update,
    name="vendor_update"
),
    

]

