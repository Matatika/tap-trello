"""REST client handling, including trelloStream base class."""

import requests

from singer_sdk.helpers.jsonpath import extract_jsonpath

from typing import Any, Dict, Optional

from memoization import cached

from singer_sdk.streams import RESTStream

from tap_trello.auth import trelloAuthenticator


class TrelloStream(RESTStream):
    """trello stream class."""

    url_base = "https://api.trello.com/1"

    records_jsonpath = "$[*]"

    limit = 1000

    @property
    @cached
    def authenticator(self) -> trelloAuthenticator:
        """Return a new authenticator object."""
        return trelloAuthenticator(self)

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
        if self.config.get("start_date", None):
            params["since"] = self.config.get("start_date")
        params["limit"] = self.limit
        if next_page_token:
            params["before"] = next_page_token
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Any:
        super().get_next_page_token(response, previous_token)

        all_matches = extract_jsonpath(f"$[{self.limit - 1}].id", response.json())

        try:
            last_element = next(iter(all_matches))
            return last_element
        except StopIteration:
            return None
