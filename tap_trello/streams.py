"""Stream type classes for tap-trello."""

from pathlib import Path
from typing import Optional

from singer_sdk import typing as th

from tap_trello.client import TrelloStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class MemberStream(TrelloStream):

    """Define member stream."""

    name = "member"
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

    parent_stream_type = MemberStream

    """Define boards stream."""
    name = "boards"
    path = "/members/{id}/boards"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "boards.json"

    replication_method = "FULL_TABLE"

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"boardId": record["id"]}


class ActionsStream(TrelloStream):

    parent_stream_type = BoardsStream

    """Define actions stream."""
    name = "actions"
    path = "/boards/{boardId}/actions"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "actions.json"

    replication_method = "INCREMENTAL"
    replication_key = "date"


class CardsStream(TrelloStream):

    parent_stream_type = BoardsStream

    """Define cards stream."""
    name = "cards"
    path = "/boards/{boardId}/cards/all"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "cards.json"

    replication_method = "FULL_TABLE"


class ChecklistsStream(TrelloStream):

    parent_stream_type = BoardsStream

    """Define checklists stream."""
    name = "checklists"
    path = "/boards/{boardId}/checklists"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "checklists.json"

    replication_method = "FULL_TABLE"


class ListsStream(TrelloStream):

    parent_stream_type = BoardsStream

    """Define lists stream."""
    name = "lists"
    path = "/boards/{boardId}/lists"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "lists.json"

    replication_method = "FULL_TABLE"


class UsersStream(TrelloStream):

    parent_stream_type = BoardsStream

    """Define users stream."""
    name = "users"
    path = "/boards/{boardId}/members"
    primary_keys = ["id"]
    schema_filepath = SCHEMAS_DIR / "users.json"

    replication_method = "FULL_TABLE"
