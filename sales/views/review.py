from django.shortcuts import redirect
from django.template.response import TemplateResponse

from sales.cart import get_cart
from sales.models import Order, OrderItem

__all__ = ["review_view", "place_order_view"]


def review_view(request):
    cart = get_cart(request)

    return TemplateResponse(
        request,
        "sales/review.html",
        {
            "cart": cart,
            "items": cart.items.all(),
            "total": cart.total,
        },
    )


def place_order_view(request):
    cart = get_cart(request)

    items = cart.items.select_related("product")

    if not items.exists():
        return redirect("sales:review")

    order = Order.objects.create(
        total_amount=cart.total
    )

    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
        )

    items.delete()
    return redirect("sales:home")
