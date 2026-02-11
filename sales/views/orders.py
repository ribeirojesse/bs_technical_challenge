from django.shortcuts import redirect

from sales.models import Order, OrderItem
from sales.cart import get_cart

__all__ = ["place_order_view"]


def place_order_view(request):
    cart = get_cart(request)

    if cart.items.count() == 0:
        return redirect("sales:products")

    order = Order.objects.create(total=cart.total)

    for item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
        )

        item.product.stock_qty -= item.quantity
        item.product.save()

    cart.items.all().delete()

    return redirect("sales:home")
