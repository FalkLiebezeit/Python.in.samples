100"""CAGR (Compound Annual Growth Rate) utilities.

This module provides a small helper to compute the compound annual growth
rate and a command-line interface for quick calculations.

Usage examples:

1. Interactive mode (no arguments):
   python CAGR-Calculation.py
   
2. Interactive mode (explicit):
   python CAGR-Calculation.py -i
   
3. Command-line mode:
   python CAGR-Calculation.py 100 155 -y 5
   
Returns:
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


def interactive_mode() -> int:
    """Run in interactive mode with user input prompts."""
    print("=== CAGR Berechnung (Interaktiver Modus) ===\n")
    
    try:
        start_value = float(input("Startwert eingeben (z.B. 100): "))
        if start_value <= 0:
            print("Fehler: Startwert muss größer als 0 sein.", file=sys.stderr)
            return 2
        
        end_value = float(input("Endwert eingeben (z.B. 155): "))
        
        years = float(input("Anzahl der Jahre eingeben (z.B. 5): "))
        if years <= 0:
            print("Fehler: Jahre müssen größer als 0 sein.", file=sys.stderr)
            return 2
        
        decimals = input("Dezimalstellen für die Ausgabe (Standard: 2): ").strip()
        decimals = int(decimals) if decimals else 2
        
        cagr = calculate_cagr(start_value, end_value, years)
        
        print(f"\n{'='*50}")
        print(f"Startwert:  {start_value:,.2f}")
        print(f"Endwert:    {end_value:,.2f}")
        print(f"Jahre:      {years}")
        print(f"{'='*50}")
        print(f"CAGR:       {format_percent(cagr, decimals=decimals)}")
        print(f"{'='*50}\n")
        
        return 0
        
    except ValueError as exc:
        print(f"Fehler: Ungültige Eingabe - {exc}", file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print("\n\nAbgebrochen.", file=sys.stderr)
        return 1


def _main(argv: Union[list[str], None] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Calculate CAGR (Compound Annual Growth Rate)",
        epilog="Ohne Argumente wird der interaktive Modus gestartet."
    )
    parser.add_argument("start", nargs='?', type=float, help="Starting value (must be > 0)")
    parser.add_argument("end", nargs='?', type=float, help="Ending value")
    parser.add_argument("--years", "-y", type=float, default=1.0, help="Number of years (default: 1)")
    parser.add_argument("--decimals", "-d", type=int, default=2, help="Decimal places for percentage output")
    parser.add_argument("--interactive", "-i", action="store_true", help="Run in interactive mode")

    args = parser.parse_args(argv)

    # Wenn keine Argumente oder --interactive, dann interaktiver Modus
    if args.interactive or (args.start is None and args.end is None):
        return interactive_mode()

    # Prüfe ob beide Werte angegeben wurden
    if args.start is None or args.end is None:
        parser.error("Startwert und Endwert müssen beide angegeben werden (oder verwenden Sie -i für interaktiven Modus)")

    try:
        cagr = calculate_cagr(args.start, args.end, args.years)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    print("CAGR:", format_percent(cagr, decimals=args.decimals))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())