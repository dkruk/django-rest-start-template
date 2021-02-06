from typing import TYPE_CHECKING

from django.contrib.auth.models import BaseUserManager

if TYPE_CHECKING:
    from user.models import User


class UserManager(BaseUserManager):
    def _create_user(
        self,
        email: str,
        first_name: str,
        password: str,
        is_staff: bool,
        is_superuser: bool,
        **extra_fields
    ) -> 'User':
        """
        Creates and saves a User with the given email and password.
        """
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, first_name: str, password: str, **extra_fields) -> 'User':
        return self._create_user(email, first_name, password, False, False, **extra_fields)

    def create_superuser(
        self,
        email: str,
        first_name: str,
        password: str,
        **extra_fields,
    ) -> 'User':
        return self._create_user(email, first_name, password, True, True, **extra_fields)
