"""Stream type classes for tap-trello."""

from pathlib import Path
from typing import Optional

from singer_sdk import typing as th

from tap_trello.client import TrelloStream

from tap_trello.schemas.actions import ActionsObject
from tap_trello.schemas.boards import BoardsObject
from tap_trello.schemas.cards import CardsObject
from tap_trello.schemas.checklists import ChecklistsObject

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class IdMemberStream(TrelloStream):

    """Define id member stream."""

    name = "stream_trello_id_member"
    path = "/members/me"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("id", th.StringType, description="The user's system ID")
    ).to_dict()

    replication_method = "FULL_TABLE"

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"id": record["id"]}


class BoardsStream(TrelloStream):

    parent_stream_type = IdMemberStream

    """Define boards stream."""
    name = "stream_trello_boards"
    path = "/members/{id}/boards"
    primary_keys = ["id"]
    schema = BoardsObject.schema

    replication_method = "FULL_TABLE"

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"idBoard": record["id"]}


class ActionsStream(TrelloStream):

    parent_stream_type = BoardsStream

    """Define actions stream."""
    name = "stream_trello_actions"
    path = "/boards/{idBoard}/actions"
    primary_keys = ["id"]

    schema = ActionsObject.schema

    replication_method = "INCREMENTAL"
    replication_key = "date"


class CardsStream(TrelloStream):

    parent_stream_type = BoardsStream

    """Define cards stream."""
    name = "stream_trello_cards"
    path = "/boards/{idBoard}/cards/all"
    primary_keys = ["id"]
    schema = CardsObject.schema

    replication_method = "FULL_TABLE"


class ChecklistsStream(TrelloStream):

    parent_stream_type = BoardsStream

    """Define checklists stream."""
    name = "stream_trello_checklists"
    path = "/boards/{idBoard}/checklists"
    primary_keys = ["id"]
    schema = ChecklistsObject.schema

    replication_method = "FULL_TABLE"


class ListsStream(TrelloStream):

    parent_stream_type = BoardsStream

    """Define lists stream."""
    name = "stream_trello_lists"
    path = "/boards/{idBoard}/lists"
    primary_keys = ["id"]

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("closed", th.BooleanType),
        th.Property("idBoard", th.StringType),
    ).to_dict()

    replication_method = "FULL_TABLE"


class MembersStream(TrelloStream):

    parent_stream_type = BoardsStream

    """Define members stream."""
    name = "stream_trello_members"
    path = "/boards/{idBoard}/members"
    primary_keys = ["id","idBoard"]

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("username", th.StringType),
        th.Property("fullName", th.StringType),
        th.Property("idBoard", th.StringType)
    ).to_dict()

    def post_process(self, row: dict, context: Optional[dict] = None) -> Optional[dict]:
        super().post_process(row, context)
        row["idBoard"] = context["idBoard"]
        return row

    replication_method = "FULL_TABLE"
