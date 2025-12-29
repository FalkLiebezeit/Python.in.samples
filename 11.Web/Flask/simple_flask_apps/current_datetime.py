#!/usr/bin/env python3
"""
Print the current local date and time.

This script prints a compact ISO-like timestamp and a human-friendly
timestamp including time zone information.
"""

from datetime import datetime


def main() -> None:
    """Get current local time and print two readable formats."""
    now = datetime.now().astimezone()

    # ISO-like format (date and time) with seconds precision
    iso_like = now.isoformat(sep=" ", timespec="seconds")

    # Human-friendly format, includes timezone name and offset when available
    human = now.strftime("%Y-%m-%d %H:%M:%S %Z%z")

    print(iso_like)
    print(human)


if __name__ == "__main__":
    main()
