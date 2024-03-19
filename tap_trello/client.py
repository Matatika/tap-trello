"""REST client handling, including TrelloStream base class."""

from memoization import cached
from singer_sdk.streams import RESTStream
from typing_extensions import override

from tap_trello.auth import TrelloAuthenticator


class TrelloStream(RESTStream):
    """trello stream class."""

    limit = 1000

    url_base = "https://api.trello.com/1"
    records_jsonpath = "$[*]"
    next_page_token_jsonpath = f"$[{limit - 1}].id"

    @property
    @cached
    @override
    def authenticator(self):
        return TrelloAuthenticator(self)

    @override
    def get_url_params(self, context, next_page_token):
        params = super().get_url_params(context, next_page_token)
        params["limit"] = self.limit

        if "start_date" in self.config:
            params["since"] = self.config.get("start_date")
        if next_page_token:
            params["before"] = next_page_token
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key

        return params
