from django.conf.urls import url

from .views import 
(
    go_menu,
    add_to_cart,
    get_pending_order,
    delete_items,
    checkout,
    success
)

app_name = 'shopping_cart'

urlpatterns = [
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^order-summary/$', order_details, name="order_summary"),
    url(r'^success/$', success, name='purchase_success'),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_items'),
    url(r'^checkout/$', checkout, name='checkout'),
    name='update_records')
]