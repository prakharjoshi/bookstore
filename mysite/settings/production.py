"""Production settings and globals."""

import os
from .base import *

# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
#from django.core.exceptions import ImproperlyConfigured


DEBUG = False

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config(default='postgres://vltroennliqmwm:Fqyvjfq3bCZja3-x-x0RZx80OY@ec2-54-197-241-96.compute-1.amazonaws.com:5432/dclibimkpak522')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration


import os
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)
