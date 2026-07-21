from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodMenu

class Order(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

    PAYMENT_METHOD = (
        ('Cash on Delivery', 'Cash on Delivery'),
    )

    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodMenu, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()

    total_price = models.IntegerField()

    order_date = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default='Pending'
    )

    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_METHOD,
        default='Cash on Delivery'
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='Pending'
    )

    def __str__(self):
        return self.user.username