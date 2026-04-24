"""Meeting-room scheduling on half-open intervals [start, end)."""

from __future__ import annotations

import heapq


def min_meeting_rooms(meetings: list[tuple[int, int]]) -> int:
    """Minimum rooms so no two overlapping meetings share a room.

    Intervals are half-open: [start, end). Touching endpoints do not overlap.
    """
    if not meetings:
        return 0
    meetings_sorted = sorted(meetings, key=lambda m: m[0])
    # Min-heap of end times of meetings currently assigned to rooms.
    heap: list[int] = []
    for start, end in meetings_sorted:
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)
    return len(heap)


def merge_busy_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping [start, end) intervals into disjoint blocks."""
    if not intervals:
        return []
    ordered = sorted(intervals, key=lambda x: x[0])
    out: list[tuple[int, int]] = [ordered[0]]
    for start, end in ordered[1:]:
        ps, pe = out[-1]
        if start < pe:
            out[-1] = (ps, max(pe, end))
        else:
            out.append((start, end))
    return out


def max_concurrent(meetings: list[tuple[int, int]]) -> int:
    """Maximum number of meetings overlapping at any instant (sweep)."""
    if not meetings:
        return 0
    events: list[tuple[int, int]] = []
    for start, end in meetings:
        events.append((start, 1))
        events.append((end, -1))
    events.sort(key=lambda e: (e[0], -e[1]))
    cur = 0
    best = 0
    for _, delta in events:
        cur += delta
        best = max(best, cur)
    return best
