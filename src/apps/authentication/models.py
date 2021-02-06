import binascii
import os

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class AuthToken(models.Model):
    key = models.CharField(_('Key'), max_length=40, primary_key=True)
    user = models.ForeignKey(
        'user.User',
        verbose_name=_('User'),
        related_name='auth_tokens',
        on_delete=models.CASCADE,
    )
    user_agent = models.CharField(_('User Agent'), max_length=1000, blank=True)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    expires_at = models.DateTimeField(_('Expires at'))

    class Meta:
        verbose_name = _('Auth Token')
        verbose_name_plural = _('Auth Tokens')

    def __str__(self) -> str:
        return f'Auth Token: {self.key}'

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @staticmethod
    def generate_key() -> str:
        return binascii.hexlify(os.urandom(20)).decode()

    @property
    def is_expired(self) -> bool:
        return self.expires_at <= timezone.now()
