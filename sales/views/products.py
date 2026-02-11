from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from sales.models import Product, CartItem
from sales.cart import get_cart

__all__ = ["product_list_view", "product_detail_view"]


def product_list_view(request):
    query = request.GET.get("q", "")
    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if request.headers.get("HX-Request") == "true":
        return TemplateResponse(
            request,
            "sales/product_list.html",
            {"products": products},
        )

    return TemplateResponse(
        request,
        "sales/products.html",
        {"products": products, "query": query},
    )



def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    cart = get_cart(request)

    cart_item = CartItem.objects.filter(
        cart=cart,
        product=product
    ).first()

    return TemplateResponse(
        request,
        "sales/product_modal.html",
        {
            "product": product,
            "cart_item": cart_item,
        },
    )
