"""
The real implementation.
"""

from django.db.models import BinaryField
import msgpack


class MsgPackField(BinaryField):
    """
    Implementation of ``django.db.models.BinaryField``, encoding data using msgpack.
    """

    # pylint: disable=no-self-use,unused-argument

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("default", None)
        super().__init__(*args, **kwargs)

    def _pack(self, value):
        """Packs value into bytes using msgpack."""
        return msgpack.dumps(value)

    def _unpack(self, value):
        """Unpacks msgpack-packed bytes."""
        if value is None:
            return None
        return msgpack.loads(value, encoding="utf8", raw=True)

    def get_prep_value(self, value):
        """Packs value as bytes for usage in db queries."""
        return super().get_prep_value(self._pack(value))

    def to_python(self, value):
        """Unpacks packed data, may also be a base64-encoded string."""
        return self._unpack(super().to_python(value))

    def deconstruct(self):
        """No need to pass ``default=None`` when reconstructing."""
        name, path, args, kwargs = super().deconstruct()
        if kwargs.get("default") is None:
            kwargs.pop("default", None)
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection, context):
        """Unpacks value after retrieval from db."""
        return self._unpack(value)

    def value_from_object(self, obj):
        """Returns packed value of this field as bytes, used for serialization."""
        return self._pack(super().value_from_object(obj))
