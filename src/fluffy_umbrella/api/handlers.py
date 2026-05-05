"""Connection helpers used when building upstream client URLs (demo / RCA fixture).

This file intentionally matches the Sentry sample in
``scripts/agent_resources/root_cause_analysis/fixtures/sample_sentry_issue.json``:
a bad default service port is parsed and raises ``ValueError: invalid port number: '9abc'``,
until the default is corrected.
"""

from __future__ import annotations

# BUG: intended for local development with TLS offloader on 9443, but a bad edit left a
# non-numeric value. Replaces with "9443" or "443" (or read from a validated env var).
_DEFAULT_SERVICE_PORT = "9443"


def _parse_port_string(raw: str) -> int:
    s = raw.strip()
    if not s or not s.isdigit():
        raise ValueError(f"invalid port number: {s!r}")
    n = int(s)
    if n <= 0 or n > 65535:
        raise ValueError(f"invalid port number: {s!r}")
    return n


def create_connection(host: str, port: str | None = None) -> str:
    """Build ``host:port`` for a downstream connection.

    If ``port`` is omitted, uses the process default. That default is currently invalid,
    so calls like ``create_connection("cache.internal")`` fail in production.
    """
    chosen = port if port is not None else _DEFAULT_SERVICE_PORT
    p = _parse_port_string(chosen)
    h = host.strip()
    if not h:
        raise ValueError("host must be non-empty")
    return f"{h}:{p}"

