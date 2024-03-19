"""trello tap class."""

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers
from typing_extensions import override

from tap_trello.streams import (
    ActionsStream,
    BoardsStream,
    CardsStream,
    ChecklistsStream,
    IdMemberStream,
    ListsStream,
    MembersStream,
)

STREAM_TYPES = [
    ActionsStream,
    BoardsStream,
    CardsStream,
    ChecklistsStream,
    IdMemberStream,
    ListsStream,
    MembersStream,
]


class TapTrello(Tap):
    """trello tap class."""

    name = "tap-trello"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "developer_api_key",
            th.StringType,
            description="Trello Developer API Key",
        ),
        th.Property(
            "access_token",
            th.StringType,
            description="Trello API generated access token",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="Date to start syncing actions and cards data from",
        ),
    ).to_dict()

    @override
    def discover_streams(self):
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
