"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import get_tap_test_class

from tap_trello.tap import TapTrello

SAMPLE_CONFIG = {}


# Run standard built-in tap tests from the SDK:
TestTapTrello = get_tap_test_class(
    tap_class=TapTrello,
    config=SAMPLE_CONFIG,
)
