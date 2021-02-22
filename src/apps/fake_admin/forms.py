
from random import uniform
from time import sleep

from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm


class FakeAdminLoginForm(AdminAuthenticationForm):

    def clean(self):
        """ Add sleep to increase wait time and always raise the default error message,
        because we don't care what they entered here.
        """

        sleep(uniform(1, 3))

        raise forms.ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': self.username_field.verbose_name}
        )
