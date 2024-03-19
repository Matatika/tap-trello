"""REST client handling, including trelloStream base class."""

from memoization import cached
from singer_sdk.streams import RESTStream
from typing_extensions import override

from tap_trello.auth import TrelloAuthenticator


class TrelloStream(RESTStream):
    """trello stream class."""

    url_base = "https://api.trello.com/1"

    records_jsonpath = "$[*]"

    limit = 1000

    # Gets the next page token with a jsonpath
    next_page_token_jsonpath = f"$[{limit - 1}].id"

    @property
    @cached
    @override
    def authenticator(self):
        return TrelloAuthenticator(self)

    @override
    def get_url_params(self, context, next_page_token):
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
