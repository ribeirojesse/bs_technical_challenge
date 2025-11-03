from django.template.response import TemplateResponse

__all__ = ["home_view"]


def home_view(request):
    return TemplateResponse(request, "sales/home.html", {})
