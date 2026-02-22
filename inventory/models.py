"""Inventory models: Category, Supplier, Product."""

from django.db import models


class Category(models.Model):
    """Organises products into logical groups (e.g. Electronics, Furniture)."""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta options for Category."""

        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return str(self.name)


class Supplier(models.Model):
    """A vendor that supplies one or more products. Added in migration 0003."""

    name = models.CharField(max_length=200)
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self) -> str:
        return str(self.name)


class Product(models.Model):
    """
    Core inventory item.

    Migration history:
        0001 – created with: name, price, category, created_at
        0002 – added: stock_count
        0003 – added: supplier (FK to Supplier)
    """

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )
    # Added in migration 0002
    stock_count = models.PositiveIntegerField(default=0)
    # Added in migration 0003
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="products",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.name)
