from __future__ import unicode_literals
from django.db import models
from accounts.models import Profile
from products.models import Product
from datetime import datetime 
from django.conf import settings

class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name
    
    def total_price(self):
        return self.price * self.quantity


class Order(models.Model):
    ref_code = models.CharField(max_length=10)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_items(self):
        book = self.items.filter(is_saved = False)
        return book

    def get_save_items(self):
        book = self.items.filter(is_saved = True)
        return book

    def get_total_price(self):
         total = 0
        for item in self.items.filter(is_saved = False):
            total += item.get_total_item_price()
             return total

    def __str__(self):
        return self.order_id

class Transaction(models.Model):
    def __init__(self, ts):
        self.shoppingCart = ts

    def getTotalTransaction(self):

        itemList = ","
        totalCost = 0.0
        while ! self.shoppingCart.isEmpty():
            itemName, costPerItem, quantity = self.shoppingCart.removeNextItem()
            itemList += (str(quantity) + " × " + str(item_id) + "\n")
            totalCost += (itemPrice * quantity)
        return itemList, totalCost

    def isValidTransaction(self):

        return self.shoppingCart.itemCount() > 0

