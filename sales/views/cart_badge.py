from django.template.response import TemplateResponse
from sales.cart import get_cart


def cart_badge_view(request):
    cart = get_cart(request)
    count = sum(item.quantity for item in cart.items.all())

    return TemplateResponse(
        request,
        "sales/cart_badge.html",
        {"cart_item_count": count},
    )
