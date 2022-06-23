"""
ASGI config for I4G00340830I project.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'I4G00340830I.settings')

application = get_asgi_application()
