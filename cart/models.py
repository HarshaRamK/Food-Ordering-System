from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodMenu

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodMenu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.food.price

    def __str__(self):
        return f"{self.user.username} - {self.food.foodname}"