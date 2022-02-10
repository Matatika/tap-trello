""" Utilities used in this module """
from tap_trello.tap import TapTrello

from singer_sdk.helpers._singer import Catalog
from singer_sdk.helpers import _catalog


SINGER_MESSAGES = []

member_return_data = {"id": "1234567890"}


def accumulate_singer_messages(message):
    """function to collect singer library write_message in tests"""
    SINGER_MESSAGES.append(message)


def set_up_tap_with_custom_catalog(mock_config, stream_list):

    tap = TapTrello(config=mock_config)
    # Run discovery
    tap.run_discovery()
    # Get catalog from tap
    catalog = Catalog.from_dict(tap.catalog_dict)
    # Reset and re-initialize with an input catalog
    _catalog.deselect_all_streams(catalog=catalog)
    for stream in stream_list:
        _catalog.set_catalog_stream_selected(
            catalog=catalog,
            stream_name=stream,
            selected=True,
        )
    # Initialise tap with new catalog
    return TapTrello(config=mock_config, catalog=catalog.to_dict())
