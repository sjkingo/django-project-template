"""
Django development settings for {{ project_name }} project.
"""

from .base import *

DEBUG = True

INTERNAL_IPS = ['127.0.0.1']

ADMINS = [
    # ('Your Name', 'your_email@example.com'),
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

# Add django-debug-toolbar
INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
