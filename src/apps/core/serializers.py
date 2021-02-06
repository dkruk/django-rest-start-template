import warnings
from typing import Type

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class DynamicFieldsSerializerMixin:
    fields: dict[str, Type[serializers.Field]]

    def __init__(self, *args, **kwargs) -> None:
        # Don't pass the 'fields' and 'exclude' args up to the superclass
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)

        # ref_name is used for API documentation generation.
        # drf_speculator ignores any fields limitations and registers all
        # Serializers with the settings that were used during the first initialization.
        # This can lead to incorrect API descriptions.
        # To avoid this set ref_name when use Serializer with fields limitations.
        self.ref_name = kwargs.pop('ref_name', None)
        if (fields or exclude) and self.ref_name is None:
            warnings.warn(
                f'Set `ref_name` to {self.__class__.__name__} where it used with '
                '`fields` or `exclude` arguments to avoid issues with API Documentation.'
            )

        if fields and exclude:
            raise Exception(_('Only one option is available at a time.'))

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)  # type: ignore

        existing = set(self.fields.keys())

        if fields is not None:
            # Drop any fields that are not specified in the 'fields' argument.
            fieldset = existing - set(fields)
            for field_name in fieldset:
                self.fields.pop(field_name, None)

        if exclude is not None:
            # Drop any fields that are specified in the 'exclude' argument.
            fieldset = existing.intersection(set(exclude))
            for field_name in fieldset:
                self.fields.pop(field_name, None)


class DynamicFieldsSerializer(DynamicFieldsSerializerMixin, serializers.Serializer):
    """
    A Serializer that takes an additional 'fields' and 'exclude' arguments that
    controls which fields should be displayed.
    """
    pass


class DynamicFieldsModelSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional 'fields' and 'exclude' arguments that
    controls which fields should be displayed.
    """

    def create(self, *args, **kwargs):
        # Do not use serializers to instantiate.
        raise Exception

    def update(self, *args, **kwargs):
        # Do not use serializers to instantiate.
        raise Exception
