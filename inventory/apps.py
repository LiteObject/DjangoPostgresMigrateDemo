"""App configuration for the inventory app."""

from django.apps import AppConfig


class InventoryConfig(AppConfig):
    """Inventory app configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "inventory"
