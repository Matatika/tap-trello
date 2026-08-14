# Copyright (c) 2026 Meltano.

"""Trello entry point."""

from __future__ import annotations

from tap_trello.tap import TapTrello

TapTrello.cli()
