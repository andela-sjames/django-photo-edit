"""
Production specific settings for GentleEdit project.
"""

from .base import *
import dj_database_url
import os

APPLICATION_DIR = os.path.dirname(globals()['__file__'])

DEBUG = True

DATABASES = {
    'default': dj_database_url.config()
}

# Enable Connection Pooling
DATABASES['default']['ENGINE'] = 'django_postgrespool'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']
