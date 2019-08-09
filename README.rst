django-msgpackfield
===================

An implementation of Django's ``BinaryField``, encoding data using msgpack.

The goal of this implementation is to be as simple and short as possible.

**NOTE:** Not to confuse with `this library on PyPi having the same name
<https://pypi.org/project/django-msgpackfield/>`_.


Installation
------------

Currently, only available from GitHub::

    pip install 'git+https://github.com/efficiosoft/django-msgpackfield@master'


Usage
-----

::

    >>> from django.db import models
    >>> from django_msgpackfield import MsgPackField
    >>>
    >>> class MyModel(Model):
    ...     data = MsgPackField()
    ...
    >>> obj = MyModel.objects.create(data={"some": "thing"})

The value of this field is ``None`` by default, unless you set something different
using the ``default=...`` keyword argument.
