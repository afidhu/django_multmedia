"""
WSGI config for MultMedia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import os


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MultMedia.settings')

application = get_wsgi_application()
