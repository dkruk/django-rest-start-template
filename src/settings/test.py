# flake8: noqa isort:skip_file
"""
This is settings not for testing server, but for unit tests.
"""

from src.settings.base import *

# Indicates that unit tests are running. Use to simplify or disable some features.
IS_TEST = True

# Don't send emails during tests.
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
EMAIL_USE_TLS = False
EMAIL_HOST = ""
EMAIL_PORT = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

# Disable throttle
REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {}
REST_FRAMEWORK["DEFAULT_THROTTLE_CLASSES"] = {}

# Week pasword hasher to make tests faster
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# Disable Sentry for tests.
sentry_sdk.init(dsn=None)
