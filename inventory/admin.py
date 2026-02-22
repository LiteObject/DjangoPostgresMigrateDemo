"""Admin registrations for the inventory app."""

from django.contrib import admin
from .models import Category, Product, Supplier


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin view for Category."""

    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Admin view for Supplier."""

    list_display = ("name", "contact_email", "phone")
    search_fields = ("name", "contact_email")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin view for Product."""

    list_display = (
        "name",
        "price",
        "stock_count",
        "category",
        "supplier",
        "created_at",
    )
    list_filter = ("category", "supplier")
    search_fields = ("name",)
