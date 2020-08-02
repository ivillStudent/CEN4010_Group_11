
from django.contrib.auth.models import User
from django.db import models
from localflavor.us.models import USStateField, USZipCodeField


# Create your models here.
class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='address')
    address = models.CharField(max_length=25, blank=True,
                               null=True, default='')
    state = USStateField()
    city = models.CharField(max_length=12,
                            null=True)
    zipcode = USZipCodeField()

    def __str__(self):
        return self.user.username


class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="creditcard", null=True)
    card_name = models.CharField(max_length=36, default='')
    card_number = models.CharField(max_length=26, default='')
    card_expirationdate = models.CharField(max_length=7, default='')
    card_ccv = models.CharField(max_length=5, default='')
