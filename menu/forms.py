from django import forms
from .models import FoodMenu

class FoodMenuForm(forms.ModelForm):

    class Meta:
        model = FoodMenu
        fields = [
        "foodname",
         "description",
        "type",
        "price",
        "foodimg",
        "Qty"
        ]