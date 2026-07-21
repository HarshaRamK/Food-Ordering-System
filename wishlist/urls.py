from django.urls import path
from . import views

urlpatterns = [

    path(
        "add/<int:id>/",
        views.add_to_wishlist,
        name="add_to_wishlist"
    ),

    path(
        "",
        views.view_wishlist,
        name="view_wishlist"
    ),

    path(
        "remove/<int:id>/",
        views.remove_wishlist,
        name="remove_wishlist"
    ),

]