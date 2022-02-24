from singer_sdk import typing as th
from tap_trello.schemas.utils.custom_schema_object import CustomObject


class ChecklistsObject(CustomObject):

    properties = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("idBoard", th.StringType),
        th.Property("idCard", th.StringType),
        th.Property("pos", th.NumberType),
        th.Property("checkItems", th.ArrayType(th.ObjectType()))
    )
