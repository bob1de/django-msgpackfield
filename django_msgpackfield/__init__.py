"""
A field that serializes/loads data using msgpack, an ultra-fast and compact binary
serialization format with more native data types than JSON.
"""

try:
    from ._field import MsgPackField
except ImportError:
    __all__ = []
else:
    __all__ = ["MsgPackField"]

__version__ = "0.1.0"
