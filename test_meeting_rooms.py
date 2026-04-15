"""Tests for meeting room scheduling (half-open intervals). Stdlib only."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "src"))

from fluffy_umbrella.meeting_rooms import (
    max_concurrent,
    merge_busy_intervals,
    min_meeting_rooms,
)


class TestMeetingRooms(unittest.TestCase):
    def test_min_meeting_rooms_cases(self) -> None:
        cases: list[tuple[list[tuple[int, int]], int]] = [
            ([], 0),
            ([(0, 1)], 1),
            ([(0, 10), (10, 20)], 1),
            ([(0, 30), (5, 10), (15, 20)], 2),
            ([(13, 15), (13, 17), (15, 17)], 2),
            ([(2, 8), (3, 4), (3, 9), (5, 11), (8, 20), (11, 14)], 3),
        ]
        for meetings, expected in cases:
            with self.subTest(meetings=meetings):
                self.assertEqual(min_meeting_rooms(meetings), expected)
                self.assertEqual(max_concurrent(meetings), expected)

    def test_merge_busy_intervals(self) -> None:
        self.assertEqual(
            merge_busy_intervals([(1, 3), (2, 6), (8, 10), (15, 18)]),
            [(1, 6), (8, 10), (15, 18)],
        )
        self.assertEqual(
            merge_busy_intervals([(1, 4), (4, 5)]),
            [(1, 4), (4, 5)],
        )


if __name__ == "__main__":
    unittest.main()
