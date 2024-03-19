"""Trello Authentication."""

from singer_sdk.authenticators import SimpleAuthenticator, SingletonMeta
from typing_extensions import override


class TrelloAuthenticator(SimpleAuthenticator, metaclass=SingletonMeta):
    """Authenticator class for Trello."""

    @property
    @override
    def oauth_request_body(self):
        return {}
