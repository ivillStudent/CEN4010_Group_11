from django.conf.urls import url

from .views import (
    home_carts,
    cart_add_book,
    remove_book,
    book_quantity,
    cart_save,
    cart_delete,
    cart_add_back,
    checkout,
    checkout_home,
    cart_Totalprice
)

urlpatterns = [
    url(r'^$', home, name='homepage'),
    url(r'^add/$', cart_add_book, name='add'),
    url(r'^remove/$', remove_book, name='remove'),
    url(r'^update_quantity/$', book_quantity, name='update_quantity'),
    url(r'^update_save/$', cart_save, name='save_for_later'),
    url(r'^remove_save/$', cart_delete, name='delete_save'),
    url(r'^add_back/$', cart_add_back, name='add_back'),
    url(r'^checkout/$', checkout, name='checkout_action'),
    url(r'^checkout_home/$', checkout_home, name='checkout_home'),
    url(r'^cart_Totalprice',cart_Totalprice, name = 'TotalPrice')
]