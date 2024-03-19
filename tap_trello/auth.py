"""Trello Authentication."""

from singer_sdk.authenticators import APIAuthenticatorBase, SingletonMeta
from typing_extensions import override


class TrelloAuthenticator(APIAuthenticatorBase, metaclass=SingletonMeta):
    """Authenticator class for Trello."""

    @property
    @override
    def auth_params(self):
        return {
            "key": self.config["developer_api_key"],
            "token": self.config["access_token"],
        }
