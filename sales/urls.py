from django.urls import path
import sales.views as views

app_name = "sales"

urlpatterns = [
    path("", views.home_view, name="home"),

    path("products/", views.product_list_view, name="products"),
    path("products/<int:pk>/", views.product_detail_view, name="product_detail"),

    path("cart/add/<int:product_id>/", views.add_to_cart_view, name="add_to_cart"),
    path("cart/update/<int:product_id>/", views.update_quantity_view, name="update_quantity"),

    path("review/", views.review_view, name="review"),

    path("cart/badge/", views.cart_badge_view, name="cart_badge"),

    path("place_order/", views.place_order_view, name="place_order"),
    path("order_history/", views.order_history_view, name="order_history"),
]
