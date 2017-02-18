"""
Django production settings for {{ project_name }} project.
"""

from .base import *

DEBUG = False

# Hosts/domain names that are valid for this site.
# See https://docs.djangoproject.com/en/1.10/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

ADMINS = [
    # ('Your Name', 'your_email@example.com'),
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'
