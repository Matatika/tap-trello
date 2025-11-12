"""Trello tap class."""

from singer_sdk import Tap
from singer_sdk import typing as th
from typing_extensions import override

from tap_trello import streams

STREAM_TYPES = [
    streams.ActionsStream,
    streams.BoardsStream,
    streams.CardsStream,
    streams.ChecklistsStream,
    streams.IdMemberStream,
    streams.ListsStream,
    streams.MembersStream,
]


class TapTrello(Tap):
    """Trello tap class."""

    name = "tap-trello"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "developer_api_key",
            th.StringType,
            required=True,
            description="Trello Developer API Key",
        ),
        th.Property(
            "access_token",
            th.StringType,
            required=True,
            description="Trello API generated access token",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="Date to start syncing actions and cards data from",
        ),
        th.Property(
            "board_ids",
            th.ArrayType(th.StringType),
            description=(
                "Optional list of board IDs to sync. "
                "If not provided, all boards will be synced."
            ),
        ),
        th.Property(
            "board_names",
            th.ArrayType(th.StringType),
            description=(
                "Optional list of board names to sync. "
                "If not provided, all boards will be synced. "
                "Case-insensitive matching."
            ),
        ),
    ).to_dict()

    @override
    def discover_streams(self):
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapTrello.cli()
