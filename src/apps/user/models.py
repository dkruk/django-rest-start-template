from typing import Optional

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import TimeStampedModel
from user.managers import UserManager


class LowerCaseEmailField(models.EmailField):
    def get_prep_value(self, value: Optional[str]) -> Optional[str]:
        value = super().get_prep_value(value)

        if value is not None:
            value = value.lower()

        return value


class User(AbstractBaseUser, TimeStampedModel, PermissionsMixin):
    email = LowerCaseEmailField(_("Email"), max_length=200, unique=True)
    is_email_confirmed = models.BooleanField(_("Email confirmed"), default=False)
    first_name = models.CharField(_("First name"), max_length=200)
    last_name = models.CharField(_("Last name"), max_length=200, blank=True)
    phone = models.CharField(_("Phone"), max_length=15, blank=True)

    is_staff = models.BooleanField(
        _("Staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("Active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list = ["first_name"]

    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.get_full_name()}({self.email})"

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
