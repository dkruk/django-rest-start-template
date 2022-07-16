import os
import sys
from pathlib import Path

import environ
from django.utils.log import DEFAULT_LOGGING

from src import __version__

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(os.path.join(PROJECT_DIR, 'apps'))

# Read environment variables
env = environ.Env(
    DEBUG=(bool, False),
    CORS_ORIGIN_ALLOW_ALL=(bool, False),
)
environ.Env.read_env(f'{BASE_DIR}/.env')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
ENVIRONMENT = env('ENVIRONMENT')
DJANGO_ADMIN_URL = env('DJANGO_ADMIN_URL')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


# Application definition
PROJECT_APPS = [
    'authentication',
    'core',
    'fake_admin',
    'user',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'django_filters',
    'rest_framework',

    *PROJECT_APPS,

    'drf_spectacular',  # Must be after all project apps.
]


AUTH_USER_MODEL = 'user.User'


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # should be placed as high as possible

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME', default='generic_form'),
        'USER': env('DATABASE_USER', default='generic_form_user'),
        'PASSWORD': env('DATABASE_PASSWORD', default='generic_form_password'),
        'HOST': env('DATABASE_HOST', default='127.0.0.1'),
        'PORT': env('DATABASE_PORT', default='5432'),
        'CONN_MAX_AGE': None,
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env('REDIS_PORT')
REDIS_DEFAULT_CACHE_DB = env('REDIS_DEFAULT_CACHE_DB')
REDIS_SESSION_DB = env('REDIS_SESSION_DB')

# Cache settings
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DEFAULT_CACHE_DB}',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'TIMEOUT': 60 * 60 * 24  # one day
    },
    'session': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_SESSION_DB}',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'TIMEOUT': 60 * 60 * 12  # 12 hours
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 24  # one day

# Save session in cache
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'session'
SESSION_COOKIE_AGE = 60 * 60 * 12  # 12 hours


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


# REST framework settings
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'authentication.auth.ApiTokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ),
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.LimitedOffsetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/second',
        'user': '1000/minute'
    },
    'DEFAULT_SCHEMA_CLASS': 'core.openapi.AutoSchema',
}


# Logging settings
# https://docs.djangoproject.com/en/3.1/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'not_local_env': {
            '()': 'core.log.RequireNotLocalEnv',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S%z'
        },
        'django.server': DEFAULT_LOGGING['formatters']['django.server'],
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'server_console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'filters': ['not_local_env'],
        },
        'logfile': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_DIR, 'project.log'),
            'maxBytes': 1024 * 1024 * 15,  # 15MB
            'backupCount': 100,
            'formatter': 'verbose',
            'filters': ['require_debug_true'],
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'django.server': DEFAULT_LOGGING['handlers']['django.server'],
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
        'django.request': {
            'handlers': ['mail_admins', 'console', 'logfile'],
            'level': 'INFO',
            'propagate': True,
        },
        'project': {
            'handlers': ['logfile', 'server_console'],
            'level': 'INFO',
            'propagate': False
        },
        'django.server': DEFAULT_LOGGING['loggers']['django.server'],
    },
}


# API Documentation settings
SPECTACULAR_SETTINGS: dict = {
    'SCHEMA_PATH_PREFIX': r'/api/v[0-9]',
    'SERVE_PUBLIC': False,
    'SERVE_PERMISSIONS': ['rest_framework.permissions.IsAdminUser'],
    'TITLE': 'API Documentation',
    'DESCRIPTION': '',
    'VERSION': __version__,
    'POSTPROCESSING_HOOKS': [
        'drf_spectacular.contrib.djangorestframework_camel_case.camelize_serializer_fields',
    ],
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
    },
    'COMPONENT_SPLIT_REQUEST': True,
}

# Means that unittests are running
IS_TEST = False
