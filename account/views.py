from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import (RegisterForm, CustomUserChangeForm,
                    AddressForm, CreditCardForm, EditAddressForm, 
                    CreditCardViewForm)
from .models import Address, CreditCard


# Create your views here.


def register(response):
    if response.method == "POST":
        register_form = RegisterForm(response.POST)
        address_form = AddressForm(response.POST)
        creditcard_form = CreditCardForm(response.POST)

        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()

        # if address_form.is_valid():
            address = address_form.save(commit=False)
            address.user = user

            # Clean Address
            address.address = address_form.cleaned_data.get('address')
            address.state = address_form.cleaned_data.get('state')
            address.city = address_form.cleaned_data.get('city')
            address.zipcodezipcode = address_form.cleaned_data.get(
                'zipcode')

            address.save()

       # if creditcard_form.is_valid():
            creditcard = creditcard_form.save(commit=False)
            creditcard.user = user

            creditcard.card_name = creditcard_form.cleaned_data.get(
                'card_name')
            creditcard.card_number = creditcard_form.cleaned_data.get(
                'card_number')
            creditcard.card_expirydate = creditcard_form.cleaned_data.get(
                'card_expirationdate')
            creditcard.card_ccv = creditcard_form.cleaned_data.get('card_ccv')

            creditcard.save()

        return redirect("/login")
    else:
        register_form = RegisterForm()
        address_form = AddressForm(instance=None)
        creditcard_form = CreditCardForm(instance=None)

    return render(response, "register.html", {"register": register_form,
                                              "address": address_form, "creditcard": creditcard_form})


@login_required
def manageAccount(response):
    try:
        address = Address.objects.get(user=response.user)
    except Address.DoesNotExist:
        address = Address(user=response.user)

    if response.method == 'POST':
        userchange_form = CustomUserChangeForm(
            data=response.POST, instance=response.user)
        address_form = EditAddressForm(response.POST, instance=address)

        if userchange_form.is_valid() or address_form.is_valid():
            userchange_form.save()
            address_form.save()

            messages.success(response, 'Profile details updated.')
            return redirect('/manageAccount')
        else:
            messages.error(response, 'Please correct the errors.')
    else:
        userchange_form = CustomUserChangeForm(instance=response.user)
        address_form = EditAddressForm(instance=address)
        args = {"userchange": userchange_form,
                'address': address_form}

    return render(response, "manageAccount.html", args)


@login_required
def viewCC(response):
    user = response.user
    return render(response, "viewCreditCard.html", {'cc_list': user.creditcard.all()})

@login_required
def createCC(response):
    if response.method == "POST":
        creditcard_form = CreditCardForm(response.POST)

        if creditcard_form.is_valid():
            creditcard = creditcard_form.save(commit=False)
            creditcard.user = response.user

            creditcard.card_name = creditcard_form.cleaned_data.get(
                'card_name')
            creditcard.card_number = creditcard_form.cleaned_data.get(
                'card_number')
            creditcard.card_expirydate = creditcard_form.cleaned_data.get(
                'card_expirationdate')
            creditcard.card_ccv = creditcard_form.cleaned_data.get('card_ccv')

            creditcard.save()

        return redirect("/viewCreditCards")
    else:
        creditcard_form = CreditCardForm(instance=None)

    return render(response, "createCreditCard.html", {"creditcard": creditcard_form})
