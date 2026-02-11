from django.test import TestCase
from django.urls import reverse
from sales.models import Product, Order 
from sales.cart import get_cart
from decimal import Decimal

class MinimalEcommerceTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Product for testing",
            price=15.0,
            stock_qty=5
        )

    def test_products_and_modal(self):
        response = self.client.get(reverse('sales:products'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

        response = self.client.get(reverse('sales:product_detail', args=[self.product.id]))
        self.assertContains(response, "Add")
        self.assertContains(response, str(self.product.price))

    def test_add_to_cart_and_review(self):
        self.client.post(reverse('sales:add_to_cart', args=[self.product.id]))
        cart = get_cart(self.client)
        self.assertEqual(cart.items.count(), 1)
        self.assertEqual(cart.items.first().quantity, 1)

        response = self.client.get(reverse('sales:review'))
        self.assertContains(response, self.product.name)
        self.assertContains(response, "15.0")

    def test_place_order_and_history(self):
        self.client.post(reverse('sales:add_to_cart', args=[self.product.id]))
        response = self.client.post(reverse('sales:place_order'))
        self.assertRedirects(response, reverse('sales:home'))

        cart = get_cart(self.client)
        self.assertEqual(cart.items.count(), 0)

        orders = Order.objects.all()
        self.assertEqual(orders.count(), 1)
        self.assertEqual(orders.first().total, Decimal('15.00'))

        response = self.client.get(reverse('sales:order_history'))
        self.assertContains(response, str(orders.first().id))
        self.assertContains(response, "15.0")
