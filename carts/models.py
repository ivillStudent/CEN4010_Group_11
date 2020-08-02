from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save, m2m_changed
from bookdetails.models import BookInfo

User = settings.AUTH_USER_MODEL

# cart manager is used to create new carts based on session and user information https://docs.djangoproject.com/en/2.0/topics/db/managers/


class CartsView(models.Model):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                user_cart = self.model.objects.filter(
                    user=request.user).first()
                if user_cart is not None:
                    cart_obj.cartItems.add(*user_cart.cartItems.all())
                    cart_obj.user = request.user
                    cart_obj.save()
                    user_cart.delete()
                else:
                    cart_obj.user = request.user
                    cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                cart_obj = self.model.objects.filter(user=user).first()
                if cart_obj is not None:
                    return cart_obj
                user_obj = user
        return self.model.objects.create(user=user_obj)


class CartItem(models.Model):
    book = models.ForeignKey(
        BookInfo, on_delete=models.CASCADE,
        related_name="book")
    quantity = models.IntegerField(
        'quantity of books',
        default=1)
    price = models.DecimalField(
        'Price of book',
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True)

    def __str__(self):
        return str(self.id)


class ItemsSaved(models.Model):
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, related_name='bookSaved')

    def __str__(self):
        return self.book.bookName


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        null=True,
        blank=True)
    cartItems = models.ManyToManyField(
        CartItem,
        blank=True)
    subtotal = models.DecimalField(
        default=0.00,
        max_digits=10,
        decimal_places=2)
    total = models.DecimalField(
        default=0.00,
        max_digits=10,
        decimal_places=2)
    updated = models.DateTimeField(
        'Last Change to Cart',
        auto_now=True)
    timestamp = models.DateTimeField(
        'Time of Cart Creation',
        auto_now_add=True)
    objects = CartsView()

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    book = models.ForeignKey(
        BookInfo, on_delete=models.CASCADE,
        related_name='purchaed_book')
    quantity = models.IntegerField(
        'quantity of books',
        default=1)
    price = models.DecimalField(
        'Price of book',
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True)
    book_price_quantity = models.DecimalField(
        'Price of Line Item: BookPrice*Quantity',
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True)

    def __str__(self):
        return '{} -- {} -- {}'.format(self.id, self.book, self.quantity)


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateTimeField(auto_now=True)

    def get_cart_items(self):
        book = self.items.filter(is_saved=False)
        return book

    def get_save_items(self):
        book = self.items.filter(is_saved=True)
        return book

    def get_total_price(self):
        total = 0
        for item in self.items.filter(is_saved=False):
            total += item.get_total_item_price()
        return total

    def get_total_save_price(self):
        total = 0
        for item in self.items.filter(is_saved=True):
            total += item.get_total_item_price()
        return total