"""
Migration 0004 – Seed Data
=====================================================
Changes:
  - Populates the database with initial Categories, Suppliers, and Products.

To apply:
    python manage.py migrate inventory 0004

To roll back to 0003:
    python manage.py migrate inventory 0003
"""

from django.db import migrations


def seed_data(apps, schema_editor):
    Category = apps.get_model("inventory", "Category")
    Supplier = apps.get_model("inventory", "Supplier")
    Product = apps.get_model("inventory", "Product")

    # Create Categories
    cat_electronics = Category.objects.create(
        name="Electronics", description="Electronic devices and accessories"
    )
    cat_furniture = Category.objects.create(
        name="Furniture", description="Home and office furniture"
    )

    # Create Suppliers
    sup_tech = Supplier.objects.create(
        name="TechCorp", contact_email="sales@techcorp.com", phone="555-0100"
    )
    sup_wood = Supplier.objects.create(
        name="WoodWorks", contact_email="hello@woodworks.com", phone="555-0200"
    )

    # Create Products
    Product.objects.create(
        name="Laptop",
        price=999.99,
        category=cat_electronics,
        stock_count=50,
        supplier=sup_tech,
    )
    Product.objects.create(
        name="Smartphone",
        price=499.99,
        category=cat_electronics,
        stock_count=150,
        supplier=sup_tech,
    )
    Product.objects.create(
        name="Office Chair",
        price=149.50,
        category=cat_furniture,
        stock_count=20,
        supplier=sup_wood,
    )
    Product.objects.create(
        name="Desk",
        price=299.00,
        category=cat_furniture,
        stock_count=10,
        supplier=sup_wood,
    )


def reverse_seed_data(apps, schema_editor):
    Category = apps.get_model("inventory", "Category")
    Supplier = apps.get_model("inventory", "Supplier")
    Product = apps.get_model("inventory", "Product")

    # Delete all seeded data
    Product.objects.all().delete()
    Supplier.objects.all().delete()
    Category.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0003_supplier"),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_seed_data),
    ]
