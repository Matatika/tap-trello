"""Trello entry point.

Copyright (c) 2026 Meltano.
"""

from __future__ import annotations

from tap_trello.tap import TapTrello

TapTrello.cli()
