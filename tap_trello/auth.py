"""trello Authentication."""


from singer_sdk.authenticators import (
    SingletonMeta,
    SimpleAuthenticator,
)


class trelloAuthenticator(SimpleAuthenticator, metaclass=SingletonMeta):
    @property
    def oauth_request_body(self) -> dict:
        """Define the OAuth request body for the trello API."""
        return {}
