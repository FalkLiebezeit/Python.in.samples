"""CAGR (Compound Annual Growth Rate) utilities.

This module provides a small helper to compute the compound annual growth
rate and a command-line interface for quick calculations.

see the following sample 

usage
CAGR-Calculation.py 100 155 -y 5

returns
CAGR: 9.16%
"""

from __future__ import annotations

import argparse
import sys
from typing import Union


def calculate_cagr(start_value: float, end_value: float, years: float) -> float:
    """Calculate the Compound Annual Growth Rate (CAGR).

    CAGR is returned as a decimal (for example 0.0912 == 9.12%).

    Parameters
    - start_value: starting value (must be > 0)
    - end_value: ending value after `years` (can be < start_value for negative CAGR)
    - years: number of years (must be > 0). Fractional years are supported.

    Raises
    - ValueError: if `start_value <= 0` or `years <= 0`.
    """
    if start_value <= 0:
        raise ValueError("start_value must be greater than zero")
    if years <= 0:
        raise ValueError("years must be greater than zero")

    return (end_value / start_value) ** (1.0 / years) - 1.0


def format_percent(value: float, decimals: int = 2) -> str:
    """Format a decimal fraction as a percentage string.

    Example: format_percent(0.09123) -> '9.12%'
    """
    return f"{value*100:.{decimals}f}%"


def _main(argv: Union[list[str], None] = None) -> int:
    parser = argparse.ArgumentParser(description="Calculate CAGR (Compound Annual Growth Rate)")
    parser.add_argument("start", type=float, help="Starting value (must be > 0)")
    parser.add_argument("end", type=float, help="Ending value")
    parser.add_argument("--years", "-y", type=float, default=1.0, help="Number of years (default: 1)")
    parser.add_argument("--decimals", "-d", type=int, default=2, help="Decimal places for percentage output")

    args = parser.parse_args(argv)

    try:
        cagr = calculate_cagr(args.start, args.end, args.years)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    print("CAGR:", format_percent(cagr, decimals=args.decimals))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())