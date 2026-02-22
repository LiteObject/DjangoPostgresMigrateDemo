# Django + PostgreSQL Migration Demo — Inventory App

A minimal Django project that demonstrates how Django migrations work step-by-step,
using an **Inventory** domain (`Product`, `Category`, `Supplier`) and PostgreSQL.

This project is ideal for learning:
- How to define Django models
- How Django's migration system tracks schema changes
- How to apply, roll back, and inspect migrations
- How to use Django Admin for data management

---

## Project Structure

```
.
├── README.md                          # This file
├── manage.py                          # Django CLI entry point
├── requirements.txt                   # Python dependencies
├── docker-compose.yml                 # PostgreSQL container config
├── .env.example                       # Environment variables template
├── .pylintrc                          # Lint configuration
├── .gitignore                         # Git ignore rules
│
├── migrate_demo/                      # Django project package
│   ├── __init__.py
│   ├── settings.py                    # Project settings (Database, Apps, etc.)
│   ├── urls.py                        # URL routing
│   └── wsgi.py                        # WSGI application entry point
│
└── inventory/                         # Django app package
    ├── __init__.py
    ├── apps.py                        # App configuration
    ├── models.py                      # Database models
    ├── admin.py                       # Admin site registration
    ├── tests.py                       # Unit tests
    ├── migrations/
    │   ├── __init__.py
    │   ├── 0001_initial.py           # Creates Category & Product
    │   ├── 0002_add_stock_count.py   # Adds stock_count field
    │   ├── 0003_supplier.py          # Creates Supplier & adds FK
    │   └── 0004_seed_data.py         # Populates initial database records
    └── tests.py                       # Unit tests
```

---

## Prerequisites

- **Python 3.11+**
- **Docker Desktop** (for running PostgreSQL)
- **Git** (to clone the repository)
- **pip** (Python package manager)

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/LiteObject/DjangoPostgresMigrateDemo.git
cd DjangoPostgresMigrateDemo
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

Edit `.env` if needed. Defaults are already configured for Docker Compose.

### 5. Start PostgreSQL

```bash
docker-compose up -d
```

Verify PostgreSQL is running:
```bash
docker-compose ps
```

### 6. Apply all migrations

```bash
python manage.py migrate
```

### 7. Create a superuser (optional)

To use the Django Admin interface:
```bash
python manage.py createsuperuser
```

Then start the development server with `python manage.py runserver` and visit http://127.0.0.1:8000/admin/.

---

## Understanding Django Migrations

### What is a migration?

A migration is a Python file that describes database schema changes. It's how Django tracks model changes
over time and applies them to your database.

**Key concepts:**

- **Migration file**: An auto-generated Python file that contains operations (e.g., `CreateModel`, `AddField`)
- **Migration state**: The current state of all migrations in your database (tracked in `django_migrations` table)
- **Forward**: Applying a migration to move *forward* in schema history
- **Backward**: Rolling back a migration to move *backward* in schema history

### The four migrations in this project

#### Migration 0001: Initial Schema
Creates two models:
- `Category` (id, name, description)
- `Product` (id, name, price, category_id, created_at)

#### Migration 0002: Add Inventory Tracking
Adds a field to track stock:
- `Product.stock_count` (PositiveIntegerField, default=0)

#### Migration 0003: Add Supplier
Introduces supplier management:
- `Supplier` (id, name, contact_email, phone)
- `Product.supplier_id` (ForeignKey to Supplier)

#### Migration 0004: Seed Data
A data migration that populates the database with initial records:
- Creates sample Categories (Electronics, Furniture)
- Creates sample Suppliers (TechCorp, WoodWorks)
- Creates sample Products linked to the categories and suppliers

**Why Data Migrations instead of Fixtures?**
This project uses a Python-based Data Migration (`RunPython`) to seed the database rather than JSON/YAML fixtures (`loaddata`). This approach is often preferred because:
1. **Automatic Execution:** Data is seeded automatically when running `python manage.py migrate`. You don't need a separate `loaddata` step.
2. **Programmability:** You can use Python logic, loops, and variables to generate data dynamically.
3. **Database Agnostic:** It relies on Django's ORM, avoiding database-specific quirks that sometimes affect raw SQL dumps.
4. **Version Control:** Python code is easier to review in pull requests than large JSON files.
5. **Rollbacks:** You can define a reverse function (like `reverse_seed_data`) to cleanly remove the seeded data if you roll back the migration.

---

## Migration Workflow

### View migration status

```bash
python manage.py showmigrations inventory
```

Example output:
```
inventory
 [X] 0001_initial
 [X] 0002_add_stock_count
 [X] 0003_supplier
 [X] 0004_seed_data
```

`[X]` = applied, `[ ]` = not yet applied

### Apply migrations step-by-step

```bash
# Apply only the first migration
python manage.py migrate inventory 0001

# Check status (0002, 0003, 0004 will show as [ ])
python manage.py showmigrations inventory

# Apply the second migration
python manage.py migrate inventory 0002

# Apply the third migration
python manage.py migrate inventory 0003

# Apply the fourth migration (seeds initial data)
python manage.py migrate inventory 0004

# Verify all are applied
python manage.py showmigrations inventory
```

### Apply all at once

```bash
python manage.py migrate
```

This applies all pending migrations in order.

### Roll back to a previous migration

```bash
# Roll back to after migration 0001 (removes 0002, 0003, and 0004)
python manage.py migrate inventory 0001

# Roll back all inventory migrations (drops all tables)
python manage.py migrate inventory zero
```

### Create a new migration

When you change a model, generate a migration:

```bash
python manage.py makemigrations inventory
```

This creates a new numbered migration file in `inventory/migrations/`.

Then apply it:

```bash
python manage.py migrate inventory
```

---

## Admin Interface

The Django Admin lets you view and edit database records via a web UI.

### Create a superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

### Run the development server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/admin/ and log in with your superuser credentials.

Navigate to:
- **Categories** → Add/edit product categories
- **Suppliers** → Add/edit suppliers
- **Products** → Add/edit inventory items

---

## Testing

Run the test suite:

```bash
python manage.py test inventory
```

Example output:
```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```

View test code in [inventory/tests.py](inventory/tests.py).

---

## Database

### Connect to PostgreSQL directly

```bash
# Using psql inside the Docker container
docker-compose exec db psql -U postgres -d inventory_db

# List all tables
\dt

# Describe the Product table
\d inventory_product

# Exit psql
\q
```

### Database URL format

The `DATABASE_URL` in `.env` follows the format:
```
postgres://username:password@host:port/database_name
```

Default: `postgres://postgres:postgres@localhost:5432/inventory_db`

---

## Troubleshooting

### "No such table" error

You haven't applied migrations yet. Run:
```bash
python manage.py migrate
```

### "Database connection refused"

PostgreSQL isn't running. Start it:
```bash
docker-compose up -d
docker-compose logs db  # Check logs if still failing
```

### "ModuleNotFoundError: No module named 'django'"

You haven't installed dependencies or activated the virtual environment:
```bash
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### Linting errors

Pylint/Pylance may complain about Django. The `.pylintrc` and `.vscode/settings.json` are configured
to suppress false positives. If errors persist:

```bash
# Ensure the venv is activated, then reload VS Code
code .
```

### How to reset the database

```bash
# Roll back all migrations
python manage.py migrate inventory zero

# Re-apply all migrations
python manage.py migrate

# This drops and recreates all inventory tables
```

---

## Development Workflow

### Make a model change

Edit [inventory/models.py](inventory/models.py):
```python
class Product(models.Model):
    # ... existing fields ...
    new_field = models.CharField(max_length=100)  # Add this
```

### Generate the migration

```bash
python manage.py makemigrations inventory
```

A new file like `0005_product_new_field.py` is created.

### Review and apply

```bash
# See what the migration does (optional, helps you understand)
python manage.py sqlmigrate inventory 0005

# Apply the migration
python manage.py migrate inventory 0005
```

### Test your changes

```bash
python manage.py test inventory
```

---

## Key Files

| File | Purpose |
|------|---------|
| [migrate_demo/settings.py](migrate_demo/settings.py) | Database, apps, middleware, secret key |
| [inventory/models.py](inventory/models.py) | Category, Supplier, Product definitions |
| [inventory/admin.py](inventory/admin.py) | Admin interface configuration |
| [inventory/migrations/](inventory/migrations/) | Migration files (version control for schema) |
| [inventory/migrations/0004_seed_data.py](inventory/migrations/0004_seed_data.py) | Data migration that seeds initial records |
| [requirements.txt](requirements.txt) | Python package dependencies |
| [docker-compose.yml](docker-compose.yml) | PostgreSQL service definition |
| [.env.example](.env.example) | Environment variables template |
| [.gitignore](.gitignore) | Git ignore rules |

---

## References

- [Django Migrations Documentation](https://docs.djangoproject.com/en/stable/topics/migrations/)
- [Django Models Documentation](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django Admin Documentation](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

## License

This project is provided as-is for educational purposes.

---

## Next Steps

- Modify the migrations to add/remove fields and learn how Django tracks changes
- Create custom migrations with data transformations (see `0004_seed_data.py` for an example)
- Explore Django's `sqlmigrate` command to see generated SQL
- Deploy to a production database and practice safe migration strategies
