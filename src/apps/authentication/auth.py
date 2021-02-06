import logging
from datetime import timedelta
from typing import TYPE_CHECKING, Final

from django.conf import settings
from django.utils import timezone
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication

from authentication.models import AuthToken

if TYPE_CHECKING:
    from user.models import User

logger = logging.getLogger('project')


class ApiTokenAuthentication(TokenAuthentication):
    THIRTY_MIN_IN_SECONDS: Final = 60 * 30
    model = AuthToken

    def authenticate_credentials(self, key: str) -> tuple['User', AuthToken]:
        now = timezone.now()
        model = self.get_model()

        try:
            token: AuthToken = model.objects\
                .select_related('user')\
                .get(key=key, expires_at__gt=now)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed

        if not token.user.is_active:
            logger.error('User, which is not active, try to login.')
            raise exceptions.AuthenticationFailed

        if (token.expires_at - now).seconds <= self.THIRTY_MIN_IN_SECONDS:
            # extend the token's validity period, to avoid logging out while
            # the User fills in the data.
            token.expires_at = now + timedelta(hours=settings.AUTH_TOKEN_LIFETIME_HOURS)
            token.save(update_fields=('expires_at',))

        return token.employee, token
