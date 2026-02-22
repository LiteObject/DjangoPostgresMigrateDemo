"""
Migration 0002 – Add stock_count to Product
=============================================
Changes:
  - Product: adds stock_count (PositiveIntegerField, default=0)

To apply:
    python manage.py migrate inventory 0002

To roll back to 0001:
    python manage.py migrate inventory 0001
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="stock_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
