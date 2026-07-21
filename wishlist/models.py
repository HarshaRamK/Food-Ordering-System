# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodMenu

class Wishlist(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodMenu, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'food')

    def __str__(self):
        return f"{self.user.username} - {self.food.foodname}"