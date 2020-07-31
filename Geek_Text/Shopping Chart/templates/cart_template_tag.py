  
from django import template
from shopping_cart.models import Order

register = template.Library()


@register.filter
def items_count(user):
    if user.is_authenticated:
        return Order.objects.filter(owner__user=user, is_ordered=False)[0].items.count()
    return 0