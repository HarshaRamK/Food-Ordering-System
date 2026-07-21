

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from orders.models import Order

class Payment(models.Model):

    PAYMENT_METHOD = (
        ('COD', 'Cash On Delivery'),
        ('UPI', 'UPI'),
        ('CARD', 'Card'),
    )
    
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_status = models.CharField(
        max_length=20,
        default="Pending"
    )

    payment_date = models.DateTimeField(
        auto_now_add=True
    )
    payment_method = models.CharField(
    max_length=30,
    default="Cash on Delivery"
    )

    payment_status = models.CharField(
        max_length=20,
        default="Pending"
    )

    

    def __str__(self):
        return self.user.username