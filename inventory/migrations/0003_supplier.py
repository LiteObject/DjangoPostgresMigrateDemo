"""
Migration 0003 – Add Supplier model + FK on Product
=====================================================
Changes:
  - Creates Supplier (name, contact_email, phone)
  - Product: adds supplier FK (nullable, SET_NULL)

To apply:
    python manage.py migrate inventory 0003

To roll back to 0002:
    python manage.py migrate inventory 0002
"""

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0002_add_stock_count"),
    ]

    operations = [
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("contact_email", models.EmailField(max_length=254)),
                ("phone", models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="supplier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="inventory.supplier",
            ),
        ),
    ]
