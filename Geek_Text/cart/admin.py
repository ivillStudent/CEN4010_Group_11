from django.contrib import admin
from .models import CartsView,Cart,CartItem,OrderItem,Order,ItemsSaved

admin.site.register(CartsView)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(ItemsSaved)
