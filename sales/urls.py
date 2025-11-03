from django.urls import path
import sales.views as views

app_name = "sales"

urlpatterns = [
    path('', views.home_view, name='home'),
]