from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from sales.models import Product, CartItem
from sales.cart import get_cart

__all__ = ["add_to_cart_view", "update_quantity_view"]


def add_to_cart_view(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)

    item, created = cart.items.get_or_create(product=product)

    if not created:
        item.quantity += 1

    item.save()

    target_id = request.GET.get("target_id", f"cart-controls-{product.id}")

    context = {
        "product": product,
        "cart_item": item,
        "target_id": target_id,
        "cart": cart,
        "toast_message": f"Added: {product.name} added to cart!",
    }

    response = TemplateResponse(
        request,
        "sales/product_cart_controls.html",
        context,
    )

    response["HX-Trigger"] = "cartUpdated"
    return response


def update_quantity_view(request, product_id):
    cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)

    quantity = int(request.POST.get("quantity", 0))
    item = CartItem.objects.filter(cart=cart, product=product).first()

    toast_message = None

    if quantity <= 0:
        if item:
            item.delete()

        item = None
        toast_message = f"Removed: {product.name} removed from cart"

    else:
        if quantity > product.stock_qty:
            quantity = product.stock_qty

        if not item:
            item = CartItem.objects.create(
                cart=cart,
                product=product,
                quantity=quantity,
            )
        else:
            item.quantity = quantity
            item.save()

        toast_message = f"Updated quantity: {product.name}"

    target_id = request.GET.get("target_id", f"cart-controls-{product.id}")

    context = {
        "product": product,
        "cart_item": item,
        "target_id": target_id,
        "cart": cart,
        "toast_message": toast_message,
    }

    response = TemplateResponse(
        request,
        "sales/product_cart_controls.html",
        context,
    )

    response["HX-Trigger"] = "cartUpdated"
    return response
