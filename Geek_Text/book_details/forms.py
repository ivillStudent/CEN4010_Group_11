from django.forms import *
from .models import Review
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Address, CreditCard
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.core.validators import validate_integer

MONTH_CHOICES = (
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)


YEAR_CHOICES = (
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024'),
    ('2025', '2025'),
    ('2026', '2026'),
    ('2027', '2027'),
    ('2028', '2028'),
    ('2029', '2029'),
    ('2030', '2030'),
    ('2031', '2031'),
    ('2032', '2032'),
    ('2033', '2033'),
    ('2034', '2034'),
)

class UserSignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    street_address = forms.CharField(max_length=100)
    apartment_address = forms.CharField(max_length=100, required=False)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=50)
    zip = forms.IntegerField(max_value=99999)
    country = CountryField(multiple=False, default='US')

    class Meta:
        model = Profile
        fields = ['nickname', 'street_address', 'apartment_address', 'city', 'state', 'zip', 'country', 'image']


class AddressForm(forms.ModelForm):
    street_address = forms.CharField(max_length=100)
    apartment_address = forms.CharField(max_length=100, required=False)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=50)
    zip = forms.IntegerField(max_value=99999)
    country = CountryField(multiple=False, default='US')
    default = forms.BooleanField(required=False)

    class Meta:
        model = Address
        fields = ['street_address', 'apartment_address', 'city', 'state', 'zip', 'country','default']
        widgets = {'country': CountrySelectWidget()}


class CreditCardForm(forms.ModelForm):
    card_number = forms.CharField(max_length=16)
    expiration_month = forms.CharField(max_length=2, widget=forms.Select(choices=MONTH_CHOICES), initial='05')
    expiration_year = forms.CharField(max_length=4, widget=forms.Select(choices=YEAR_CHOICES), initial='01')
    security_code = forms.IntegerField(max_value=9999)
    cardholder_name = forms.CharField(max_length=100)
    default = forms.BooleanField(required=False)
    
    class Meta:
        model = CreditCard
        fields = ['card_number', 'expiration_month', 'expiration_year', 'security_code', 'cardholder_name', 'default']

    def clean_card_number(self, *args, **kwargs):
        card_number = self.cleaned_data.get("card_number")
        if validate_integer(card_number):
            raise forms.ValidationError("This is not a valid credit card number")
        if len(card_number) != 16:
            raise forms.ValidationError("This is not a valid credit card number")
        return card_number