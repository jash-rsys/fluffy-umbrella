"""Run a small demo: `python -m fluffy_umbrella`."""

from __future__ import annotations

from fluffy_umbrella.meeting_rooms import min_meeting_rooms


def main() -> None:
    sample = [
        (0, 30),
        (5, 10),
        (15, 20),
    ]
    rooms = min_meeting_rooms(sample)
    print("meetings:", sample)
    print("min_meeting_rooms:", rooms)


if __name__ == "__main__":
    main()
