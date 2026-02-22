"""WSGI config for the migrate_demo project."""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "migrate_demo.settings")

application = get_wsgi_application()
