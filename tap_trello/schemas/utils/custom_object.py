"""Base custom object defintion."""

from singer_sdk import typing as th
from typing_extensions import override

# ruff: noqa: N805


class CustomObject(th.JSONTypeHelper):
    """Custom object."""

    properties: th.PropertiesList

    @th.DefaultInstanceProperty
    @override
    def type_dict(cls):
        return cls.properties.to_dict()

    @th.DefaultInstanceProperty
    def schema(cls):  # noqa: D102
        return cls.type_dict
