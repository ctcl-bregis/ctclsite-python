# ctclsite-python - CTCL 2020-2023
# File: asgi.py
# Purpose: ASGI interface
# Created: August 26, 2023
# Modified: August 27, 2023

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_asgi_application()
