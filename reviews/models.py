
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from menu.models import FoodMenu


class Review(models.Model):

    RATING = (
        (1, "1 Star"),
        (2, "2 Stars"),
        (3, "3 Stars"),
        (4, "4 Stars"),
        (5, "5 Stars"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodMenu, on_delete=models.CASCADE)

    rating = models.IntegerField(choices=RATING)

    review = models.TextField()

    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username