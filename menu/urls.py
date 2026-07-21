from django.urls import path
from . import views

urlpatterns = [

    path('menu-building/', views.menubuilding,name='menubuilding'),

    path('food-list/', views.foodlist, name='foodlist'),

    path('update-food/<int:id>/', views.updatefood, name='updatefood'),

    path('delete-food/<int:id>/', views.deletefood, name='deletefood'),
    
    path("food/<int:id>/", views.food_details, name="food_details"),
]