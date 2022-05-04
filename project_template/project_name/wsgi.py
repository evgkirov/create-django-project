"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from {{ project_name }}.settings.utils import env


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "{{ project_name }}.settings.{}".format(env("ENVIRONMENT", default="development")),
)

application = get_wsgi_application()
