# fluffy-umbrella

A small Python exercise focused on **interval scheduling** and **priority queues**. The core problem is computing the **minimum number of meeting rooms** needed when each meeting has a start and end time (half-open intervals `[start, end)`).

## Why this repo exists

This directory is a **sample GitHub-style project** for agent and workflow testing: realistic layout (`src/`, `tests/`, `.github/workflows/`), a `README` with a clear contract, and non-trivial edge cases in the test suite.

**No third-party dependencies** — standard library only.

### RCA / Sentry-style incident (for E2E)

`src/fluffy_umbrella/api/handlers.py` defines `create_connection` and a bad default port string that raises
`ValueError: invalid port number: '9abc'` when the port is omitted — the same message as
`scripts/agent_resources/root_cause_analysis/fixtures/sample_sentry_issue.json`.
Point the RCA agent at this repo and that fixture (or a matching inbound webhook) to reproduce
the error in code and land a small PR (e.g. set `_DEFAULT_SERVICE_PORT` to a valid value such as
`"9443"` or read from a validated environment variable).

## Run

Requires **Python 3.12+**. From this directory:

```bash
# Demo
python run_demo.py

# Tests (stdlib unittest)
python -m unittest discover -s tests -p "test_*.py" -v
```

## Problem statement

You are given a list of meetings `meetings[i] = (start_i, end_i)` where times are integers on the same day (minutes since midnight, for example). Meetings use **half-open** intervals: `[start, end)` — the end time is exclusive, so `(10, 20)` and `(20, 30)` do **not** overlap.

Implement:

- `min_meeting_rooms(meetings: list[tuple[int, int]]) -> int`  
  Return the minimum number of rooms such that no two overlapping meetings share a room.

## Stretch goals (optional)

1. **`merge_busy_intervals`** — merge overlapping busy intervals into disjoint blocks.
2. **`max_concurrent(meetings)`** — return the maximum overlap count (same answer as the heap peak for valid inputs, but useful to cross-check).

The reference implementation lives in `src/fluffy_umbrella/meeting_rooms.py`.

## Repository layout

```
fluffy-umbrella/
├── README.md                 # This file
├── LICENSE                   # MIT
├── run_demo.py               # Demo entry (adds src/ to path)
├── src/
│   └── fluffy_umbrella/
│       ├── __init__.py
│       ├── __main__.py       # Module CLI: needs PYTHONPATH=src
│       ├── meeting_rooms.py  # Core algorithms
│       └── api/
│           ├── __init__.py
│           └── handlers.py  # `create_connection` (RCA sample: bad default port)
├── tests/
│   ├── test_meeting_rooms.py # unittest
│   └── test_handlers.py
└── .github/
    └── workflows/
        └── ci.yml            # unittest on push/PR
```

## License

MIT — see `LICENSE`.
