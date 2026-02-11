from sales.cart import get_cart


def cart_item_count(request):
    cart = get_cart(request)
    count = sum(item.quantity for item in cart.items.all())

    return {"cart_item_count": count}
