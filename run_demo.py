"""Run the demo without installing the package (stdlib only)."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from fluffy_umbrella.__main__ import main

if __name__ == "__main__":
    main()
