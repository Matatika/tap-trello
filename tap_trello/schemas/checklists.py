"""Schema definitions for checklists objects."""

from singer_sdk import typing as th

ChecklistsObject = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("name", th.StringType),
    th.Property("idBoard", th.StringType),
    th.Property("idCard", th.StringType),
    th.Property("pos", th.NumberType),
    th.Property("checkItems", th.ArrayType(th.ObjectType())),
)
