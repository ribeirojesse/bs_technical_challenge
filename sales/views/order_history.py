from django.template.response import TemplateResponse
from sales.models import Order

__all__ = ["order_history_view"]


def order_history_view(request):
    orders = Order.objects.all().order_by("-created_at")

    return TemplateResponse(
        request,
        "sales/order_history.html",
        {"orders": orders},
    )
