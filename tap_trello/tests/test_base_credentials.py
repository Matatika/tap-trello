"""Tests the tap using a mock base credentials config."""

import unittest
import responses
import singer

from tap_trello.tap import TapTrello, TapTrello

import tap_trello.tests.utils as test_utils


class TestTapTrelloWithBaseCredentials(unittest.TestCase):
    """Test class for tap-trello using base credentials"""

    def setUp(self):
        self.mock_config = {
            "developer_api_key": "1234",
            "oauth_secret": "1234",
            "access_token": "1234",
        }
        responses.reset()
        del test_utils.SINGER_MESSAGES[:]

        singer.write_message = test_utils.accumulate_singer_messages

    def test_base_credentials_discovery(self):
        """Test basic discover sync"""

        catalog = TapTrello(self.mock_config).discover_streams()

        # expect valid catalog to be discovered
        self.assertEqual(len(catalog), 2, "Total streams from default catalog")

    @responses.activate
    def test_trello_sync_member(self):
        """Test sync."""

        tap = test_utils.set_up_tap_with_custom_catalog(self.mock_config, ["member"])

        responses.add(
            responses.GET,
            "https://api.trello.com/1/members/me",
            json=test_utils.member_return_data,
            status=200,
        )

        tap.sync_all()

        self.assertEqual(len(test_utils.SINGER_MESSAGES), 3)
        self.assertIsInstance(test_utils.SINGER_MESSAGES[0], singer.SchemaMessage)
        self.assertIsInstance(test_utils.SINGER_MESSAGES[1], singer.RecordMessage)
        self.assertIsInstance(test_utils.SINGER_MESSAGES[2], singer.StateMessage)
