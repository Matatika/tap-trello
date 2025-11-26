"""Stream type classes for tap-trello."""

from singer_sdk import typing as th
from singer_sdk.streams.core import REPLICATION_INCREMENTAL
from typing_extensions import override

from tap_trello.client import TrelloStream
from tap_trello.schemas.actions import ActionsObject
from tap_trello.schemas.boards import BoardsObject
from tap_trello.schemas.cards import CardsObject
from tap_trello.schemas.checklists import ChecklistsObject


class IdMemberStream(TrelloStream):
    """Define ID member stream."""

    name = "stream_trello_id_member"
    path = "/members/me"
    primary_keys = ("id",)
    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The user's system ID",
        ),
    ).to_dict()

    @override
    def get_child_context(self, record, context):
        return {"id": record["id"]}


class BoardsStream(TrelloStream):
    """Define boards stream."""

    parent_stream_type = IdMemberStream
    name = "stream_trello_boards"
    path = "/members/{id}/boards"
    primary_keys = ("id",)
    schema = BoardsObject.to_dict()

    @override
    def get_child_context(self, record, context):
        return {"idBoard": record["id"]}

    @override
    def post_process(self, row, context=None):
        """Filter boards based on board_ids configuration."""
        row = super().post_process(row, context)

        # Get filtering configuration
        board_ids = self.config.get("board_ids", [])

        # filter by board IDs if configured, or else return all boards
        return row if not board_ids or row["id"] in board_ids else None


class ActionsStream(TrelloStream):
    """Define actions stream."""

    parent_stream_type = BoardsStream
    name = "stream_trello_actions"
    path = "/boards/{idBoard}/actions"
    primary_keys = ("id",)
    schema = ActionsObject.to_dict()

    replication_method = REPLICATION_INCREMENTAL
    replication_key = "date"


class CardsStream(TrelloStream):
    """Define cards stream."""

    parent_stream_type = BoardsStream
    name = "stream_trello_cards"
    path = "/boards/{idBoard}/cards/all"
    primary_keys = ("id",)
    schema = CardsObject.to_dict()


class ChecklistsStream(TrelloStream):
    """Define checklists stream."""

    parent_stream_type = BoardsStream
    name = "stream_trello_checklists"
    path = "/boards/{idBoard}/checklists"
    primary_keys = ("id",)
    schema = ChecklistsObject.to_dict()


class ListsStream(TrelloStream):
    """Define lists stream."""

    parent_stream_type = BoardsStream
    name = "stream_trello_lists"
    path = "/boards/{idBoard}/lists"
    primary_keys = ("id",)

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("closed", th.BooleanType),
        th.Property("idBoard", th.StringType),
    ).to_dict()


class MembersStream(TrelloStream):
    """Define members stream."""

    parent_stream_type = BoardsStream
    name = "stream_trello_members"
    path = "/boards/{idBoard}/members"
    primary_keys = ("id", "idBoard")

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("username", th.StringType),
        th.Property("fullName", th.StringType),
        th.Property("idBoard", th.StringType),
    ).to_dict()

    @override
    def post_process(self, row, context=None):
        row = super().post_process(row, context)
        row["idBoard"] = context["idBoard"]

        return row
