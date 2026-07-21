from django.db import models

# Create your models here.
# class FoodMenu(models.Model):
#     food_types=[('VEG','veg'),('NONVEG','nonveg')]
#     foodname=models.CharField(max_length=100)
#     type=models.CharField(max_length=100,choices=food_types)
#     price=models.IntegerField() 
#     foodimg=models.ImageField(upload_to='foodimg/',blank=None,null=None)
#     Qty=models.CharField(max_length=100)

from accounts.models import VendorDetails

class FoodMenu(models.Model):

    restaurant = models.ForeignKey(
        VendorDetails,
        on_delete=models.CASCADE,null=True,
    blank=True
    )

    food_types = [
        ('VEG', 'veg'),
        ('NONVEG', 'nonveg')
    ]

    foodname = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=food_types)
    price = models.IntegerField()
    foodimg = models.ImageField(upload_to='foodimg/')
    Qty = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True, null=True)