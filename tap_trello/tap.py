"""trello tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_trello.streams import (
    TrelloStream,
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

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
