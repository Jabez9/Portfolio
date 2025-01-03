"""
WSGI config for Huya project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise

# from Huya import portapp

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Huya.settings')

application = get_wsgi_application()


application = WhiteNoise(application, root="static/")