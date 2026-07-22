from django import forms
from django.contrib.auth.models import User
from accounts.models import UserDetails,VendorDetails
from django_recaptcha.fields import ReCaptchaField

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        # fields="__all__"
        fields =['username','email','password']


class UserProfileForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = UserDetails
        fields =['phone','house_no','address','city','state','zipcode','userpic']

class VendorForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','email','password']

class VendorProfileForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = VendorDetails
        fields =['RestaurentName','LICNo','GSTNo','LIC_Certificate',
                  'Restaurent_email','Restaurent_phone','Restaurent_address','landmark',
                  'zipcode','Restaurent_img']



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=UserDetails
        fields=['phone','house_no','address','city','state','zipcode','userpic']
   
class VendorProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = VendorDetails
        fields = [
            "RestaurentName",
            "LICNo",
            "GSTNo",
            "Restaurent_email",
            "Restaurent_phone",
            "Restaurent_address",
            "landmark",
            "zipcode",
            "Restaurent_img",
            "LIC_Certificate",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"