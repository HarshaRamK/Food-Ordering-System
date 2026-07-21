from django.contrib import admin

# Register your models here.
from accounts.models import *
admin.site.register(UserDetails)
admin.site.register( VendorDetails)


