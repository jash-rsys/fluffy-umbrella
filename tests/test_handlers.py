"""Tests for `api.handlers` (connection DSN / port parsing)."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from fluffy_umbrella.api.handlers import create_connection, _parse_port_string


class TestHandlers(unittest.TestCase):
    def test_parse_port_accepts_valid_and_rejects_malformed(self) -> None:
        self.assertEqual(_parse_port_string("443"), 443)
        self.assertEqual(_parse_port_string(" 8080 "), 8080)
        with self.assertRaisesRegex(ValueError, r"invalid port number: '9abc'"):
            _parse_port_string("9abc")

    def test_create_connection_explicit_port_succeeds(self) -> None:
        self.assertEqual(create_connection("db.internal", "5432"), "db.internal:5432")
        self.assertEqual(create_connection(" cache.internal ", " 11211 "), "cache.internal:11211")

    def test_create_connection_omitted_port_uses_default_and_may_fail(
        self,
    ) -> None:
        # Matches Sentry: ValueError: invalid port number: '9abc' until the default
        # in handlers.py is a valid numeric string (e.g. "9443").
        with self.assertRaisesRegex(
            ValueError, r"invalid port number: '9abc'"
        ):
            create_connection("any-host")


if __name__ == "__main__":
    unittest.main()
