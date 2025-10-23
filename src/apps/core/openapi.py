from typing import TYPE_CHECKING

from drf_spectacular.openapi import AutoSchema as BaseAutoSchema

if TYPE_CHECKING:
    from rest_framework.serializers import Serializer


class AutoSchema(BaseAutoSchema):
    """
    Custom AutoSchema for correct work Dynamic Serializers.
    """

    def _get_serializer_name(
        self,
        serializer: type["Serializer"],
        direction: str,
        bypass_extensions: bool = False,
    ) -> str:
        if getattr(serializer, "ref_name", None) is not None:
            return serializer.ref_name

        return super()._get_serializer_name(serializer, direction, bypass_extensions)
