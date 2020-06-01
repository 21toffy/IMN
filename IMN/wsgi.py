"""
WSGI config for IMN project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise

from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IMN.settings")

application = get_wsgi_application()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

application = WhiteNoise(application, root=os.path.join(BASE_DIR,'/static'))

# application = DjangoWhiteNoise(application)
