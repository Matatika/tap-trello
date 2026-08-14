"""Schema definitions for actions objects."""

from singer_sdk import typing as th

ActionsObject = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("idMemberCreator", th.StringType),
    th.Property(
        "data",
        th.ObjectType(
            th.Property(
                "card",
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType),
                    th.Property("desc", th.StringType),
                    th.Property("idList", th.StringType),
                    th.Property("idShort", th.NumberType),
                    th.Property("shortLink", th.StringType),
                ),
            ),
            th.Property(
                "old",
                th.ObjectType(
                    th.Property("name", th.StringType),
                    th.Property("desc", th.StringType),
                    th.Property("idList", th.StringType),
                ),
            ),
            th.Property(
                "board",
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType),
                    th.Property("shortLink", th.StringType),
                ),
            ),
            th.Property(
                "list",
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType),
                ),
            ),
            th.Property(
                "listBefore",
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType),
                ),
            ),
            th.Property(
                "listAfter",
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType),
                ),
            ),
            th.Property(
                "checklist",
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType),
                ),
            ),
            th.Property(
                "checkItem",
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType),
                    th.Property("state", th.StringType),
                ),
            ),
        ),
    ),
    th.Property("appCreator", th.BooleanType),
    th.Property("type", th.StringType),
    th.Property("date", th.StringType),
    th.Property("limits", th.ObjectType()),
    th.Property(
        "memberCreator",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("activityBlocked", th.BooleanType),
            th.Property("fullName", th.StringType),
            th.Property("initials", th.StringType),
            th.Property("username", th.StringType),
        ),
    ),
)
