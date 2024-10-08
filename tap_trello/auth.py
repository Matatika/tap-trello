"""Trello Authentication."""

from singer_sdk.authenticators import APIAuthenticatorBase, SingletonMeta
from typing_extensions import override


class TrelloAuthenticator(APIAuthenticatorBase, metaclass=SingletonMeta):
    """Authenticator class for Trello."""

    @override
    def __init__(self, stream) -> None:
        super().__init__(stream)
        self.auth_params = {
            "key": self.config["developer_api_key"],
            "token": self.config["access_token"],
        }
