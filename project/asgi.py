"""
ASGI config for project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

import channels
import django
from django.core.asgi import get_asgi_application

from .urls import asgi_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
asgi_app = get_asgi_application()


application = channels.routing.ProtocolTypeRouter(
    {
        "http": asgi_app,
        "websocket": channels.routing.URLRouter(asgi_urlpatterns),
    }
)
