from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from localflavor.us.forms import USStateSelect, USZipCodeField
from .models import Address, CreditCard




class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = get_user_model()
        fields = ["email","first_name", "last_name", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.username = user.email

        if commit:
            user.save()

        return user

class AddressForm(forms.ModelForm):
    address = forms.CharField(max_length=20, required=True)
    state = USStateSelect()
    city = forms.CharField(max_length=20)
    zipcode = USZipCodeField()

    class Meta:
        model = Address
        fields = ('address', 'state', 'city', 'zipcode')

    def save(self, commit=True):
        address = super().save(commit=False)
        address.address = self.cleaned_data.get('address')
        address.state = self.cleaned_data.get('state')
        address.city = self.cleaned_data.get('city')
        address.zipcode = self.cleaned_data.get('zipcode')

        if commit:
            address.save()

        return address

class CreditCardForm(forms.ModelForm):
    card_name = forms.CharField(max_length=36)
    card_number = forms.CharField(max_length=26)
    card_expirationdate = forms.CharField(max_length=7)
    card_ccv = forms.CharField(max_length=5)

    class Meta:
        model = CreditCard
        fields = ('card_name', 'card_number', 'card_expirationdate', 'card_ccv')

    def save(self, commit=True):
        creditcard = super().save(commit=False)
        creditcard.card_name = self.cleaned_data.get('card_name')
        creditcard.card_number = self.cleaned_data.get('card_number')
        creditcard.card_expirydate = self.cleaned_data.get('card_expirationdate')
        creditcard.card_ccv = self.cleaned_data.get('card_ccv')

        if commit:
            creditcard.save()

        return creditcard


class CustomUserChangeForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["first_name", "last_name"]
        read_only_fields = ("email", "username")

class AddressViewForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('address', 'state', 'city', 'zipcode')
        exclude = ('user',)

class CreditCardViewForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ('card_name', 'card_number', 'card_expirationdate', 'card_ccv')
        exclude = ('user',)

class EditAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ("address", "state", "city", "zipcode")

class EditCreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ('card_name', 'card_number', 'card_expirationdate', 'card_ccv')


