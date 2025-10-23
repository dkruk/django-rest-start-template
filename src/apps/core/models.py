from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-managed "created_at" and "updated_at" fields.
    created_at - automatically set the field to now when the object is first created.
    updated_at - automatically set the field to now every time the object is saved.
    """

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        abstract = True
