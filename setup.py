#!/usr/bin/env python

from setuptools import find_packages, setup

from django_msgpackfield import __version__


setup(
    name="django-msgpackfield",
    version=__version__,
    description="Django database field encoding data using msgpack",
    long_description=open("README.rst").read(),
    author="Robert Schindler",
    author_email="r.schindler@efficiosoft.com",
    url="https://github.com/efficiosoft/django-msgpackfield",
    license="MIT License",
    packages=find_packages("."),
    install_requires=("django ~= 2.0", "msgpack ~= 0.6"),
)
