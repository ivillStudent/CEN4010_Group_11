  
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from account.models import Profile
from bookdetails.models import BookInfo
from shopping_cart.extras import generate_order_id, transact, generate_client_token
from shopping_cart.models import OrderItem, Order, Transaction
import datetime
import stripe



def go_menu(self):
    print('=' * 30)
    print('\33[34;1m1.shopping')
    print('2.Delete from the shopping chart')
    print('3.Checkout')
    print('4.Exit\33[1m')
    print('=' * 30)

    while True:
            self.go = input('Enter your choice:')
            if self.go == '1':
                self.shopping_car()
                break
            elif self.go == '2':
                self.del_goods()
                break
            elif self.go == '3':
                self.jiezhang()
                break
            elif self.go == '4':
                break
            else:
                print('The input is wrong, please try again:')

# Shopping
@login_required()
def add_to_cart(self, **kwargs):
   
    user_profile = get_object_or_404(Profile, user=self.user)
    
    product = Product.objects.filter(id=kwargs.get('item_id', "")).first()
    
    if product in self.user.profile.ebooks.all():
        messages.info(self, 'You already own this ebook')
        return redirect(reverse('products:product-list')) 
    
    order_item, status = OrderItem.objects.get_or_create(product=product)
   
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        
        user_order.ref_code = generate_order_id()
        user_order.save()

    
    messages.info(self, "item added to cart")
    return redirect(reverse('products:product-list'))

# Get items
def get_pending_order(self):
    user_profile = get_object_or_404(Profile, user=self.user)
    order = Order.objects.filter(owner=user_profile)
    if order.exists():
        return order[0]
        return 0

# Delete items
@login_required()
def delete_items(self, item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(self, "The book has been removed")
        return redirect(reverse('shopping_cart:order_summary'))

# CheckOut
@login_required()
def checkout(self,**kwargs):
    OrderItem.objects.filter(is_saved=False).delete()
    messages.info(self, "Thank you for your business, have a good day!")
    return redirect(reverse('shopping_cart:order_summary'))


def success(self, **kwargs):
    # a view signifying the transcation was successful
    return render(self, 'shopping_cart/purchase_success.html', {})