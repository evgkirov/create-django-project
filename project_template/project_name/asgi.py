"""
ASGI config for {{ project_name }} project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from {{ project_name }}.settings.utils import env


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "{{ project_name }}.settings.{}".format(env("ENVIRONMENT", default="development")),
)

application = get_asgi_application()
