from drf_spectacular.openapi import AutoSchema as BaseAutoSchema


class AutoSchema(BaseAutoSchema):
    """
    Custom AutoSchema for correct work Dynamic Serializers.
    """

    def _get_serializer_name(self, serializer, direction):
        if getattr(serializer, 'ref_name', None) is not None:
            return serializer.ref_name

        return super()._get_serializer_name(serializer, direction)
