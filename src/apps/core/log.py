import logging

from django.conf import settings

from src.global_constants import LOCAL_ENV


class RequireNotLocalEnv(logging.Filter):
    def filter(self, record):
        return settings.ENVIRONMENT != LOCAL_ENV
