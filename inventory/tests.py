"""Tests for the inventory app models."""

from django.test import TestCase
from .models import Category, Product, Supplier


class CategoryModelTest(TestCase):  # pylint: disable=no-member
    """Tests for the Category model."""

    def test_str(self):
        """Category __str__ returns the category name."""
        cat = Category.objects.create(name="Electronics")  # pylint: disable=no-member
        self.assertEqual(str(cat), "Electronics")


class ProductModelTest(TestCase):  # pylint: disable=no-member
    """Tests for the Product model."""

    def test_str(self):
        """Product __str__ returns the product name."""
        product = Product.objects.create(
            name="Laptop", price="999.99"
        )  # pylint: disable=no-member
        self.assertEqual(str(product), "Laptop")

    def test_default_stock_count(self):
        """Product stock_count defaults to 0 on creation."""
        product = Product.objects.create(
            name="Mouse", price="19.99"
        )  # pylint: disable=no-member
        self.assertEqual(product.stock_count, 0)


class SupplierModelTest(TestCase):  # pylint: disable=no-member
    """Tests for the Supplier model."""

    def test_str(self):
        """Supplier __str__ returns the supplier name."""
        supplier = Supplier.objects.create(  # pylint: disable=no-member
            name="Acme Corp", contact_email="acme@example.com"
        )
        self.assertEqual(str(supplier), "Acme Corp")
