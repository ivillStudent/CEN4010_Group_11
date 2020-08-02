from django.contrib import admin
from django.contrib.auth.models import UserManager
from .models import Address, CreditCard

# Register your models here.
admin.site.register(Address)
admin.site.register(CreditCard)