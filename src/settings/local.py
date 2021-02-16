"""
Settings for local development.
"""

from src.settings.base import *

# Disable Sentry
RAVEN_CONFIG = {}

# Add Django debug tool bar
INSTALLED_APPS.append('debug_toolbar')
MIDDLEWARE.insert(1, 'debug_toolbar.middleware.DebugToolbarMiddleware')
INTERNAL_IPS = [
    '127.0.0.1',
]

# Switch on Browser render to display debug panel.
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (  # type: ignore
    'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
) + REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES']

REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'] = (  # type: ignore
    'rest_framework.authentication.SessionAuthentication',
) + REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']
