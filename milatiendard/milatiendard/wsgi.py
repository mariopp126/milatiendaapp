"""
WSGI config for milatiendard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
environment = os.getenv('DJANGO_ENV', 'development')

if environment == 'production':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'milatiendard.settings_prod'
elif environment == 'staging':
    os.environ['DJANGO_SETTINGS_MODULE'] = 'milatiendard.settings_local'

from django.core.management import execute_from_command_line

application = get_wsgi_application()
