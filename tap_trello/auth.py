# Copyright (c) 2026 Meltano.

"""Trello Authentication."""

from singer_sdk.authenticators import APIAuthenticatorBase, SingletonMeta


class TrelloAuthenticator(APIAuthenticatorBase, metaclass=SingletonMeta):
    """Authenticator class for Trello."""

    def __init__(self, stream) -> None:
        """Initialise the authenticator from the stream config.

        Args:
            stream: The stream that uses the authenticator.
        """
        super().__init__()
        self.auth_params = {
            "key": stream.config["developer_api_key"],
            "token": stream.config["access_token"],
        }
