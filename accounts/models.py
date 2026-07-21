#It handle sql related quries
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)


# Additional fields
    phone =models.BigIntegerField()
    house_no = models.IntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    userpic = models.ImageField(upload_to='userimg/',blank=True,null=True)

    def __str__(self):
        return self.user.username

class VendorDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

# Additional fields
    RestaurentName=models.CharField(max_length=100)
    LICNo=models.CharField(max_length=100)
    GSTNo=models.CharField(max_length=100)
    LIC_Certificate=models.ImageField(upload_to='lic_certi/')
    Restaurent_email=models.EmailField(max_length=100)
    Restaurent_phone=models.IntegerField()
    Restaurent_address=models.CharField(max_length=100)
    landmark=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    Restaurent_img=models.ImageField(upload_to='restimg/')
    is_approved=models.BooleanField(default=False)

    def __str__(self):
        return self.RestaurentName
    


    