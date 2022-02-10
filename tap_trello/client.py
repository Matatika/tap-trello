"""REST client handling, including trelloStream base class."""

from typing import Any, Dict, Optional

from memoization import cached

from singer_sdk.streams import RESTStream

from tap_trello.auth import trelloAuthenticator, trelloSimpleAuth


class TrelloStream(RESTStream):
    """trello stream class."""

    url_base = "https://api.trello.com/1"

    records_jsonpath = "$[*]"
    next_page_token_jsonpath = "$.next_page"

    @property
    @cached
    def authenticator(self) -> trelloAuthenticator:
        """Return a new authenticator object."""
        return trelloSimpleAuth(self)

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        return {}

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        params["key"] = self.config.get("developer_api_key")
        params["token"] = self.config.get("access_token")
        if next_page_token:
            params["page"] = next_page_token
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params
