"""Printer status tool (English, improved).

This script performs a quick health check for a network printer and optionally
queries SNMP (v2c) for details. It is written to be safe to run even when
`pysnmp` is not installed — the reachability check will still work.

Typical usage:
	python printerstatus.py --ip 10.24.10.12

To enable SNMP queries, install `pysnmp` into the project's virtualenv:
	C:\\Users\\Falk\\source\\repos\\Python.in.samples\\Python.in.samples\\Scripts\\python.exe -m pip install pysnmp
"""

from __future__ import annotations

import argparse
import socket
import sys
from typing import List, Optional, Tuple

DEFAULT_SNMP_COMMUNITY = "public"
PRINTER_MIB_OID = "1.3.6.1.2.1.43"  # Printer-MIB base OID


def check_tcp_port(ip: str, port: int = 9100, timeout: float = 2.0) -> bool:
	"""Return True when a TCP connection to (ip, port) succeeds within timeout."""
	try:
		with socket.create_connection((ip, port), timeout=timeout):
			return True
	except Exception:
		return False


def pysnmp_available() -> bool:
	"""Return True if pysnmp.hlapi is importable.

	We check the specific submodule used by this script so the availability
	test is meaningful for the functions below.
	"""
	try:
		import pysnmp.hlapi  # type: ignore
		return True
	except Exception:
		return False


def snmp_get(ip: str, oid: str, community: str = DEFAULT_SNMP_COMMUNITY, timeout: int = 2) -> Optional[Tuple[str, str]]:
	"""Perform an SNMPv2c GET for a single OID and return (oid, value).

	Raises RuntimeError when pysnmp is not available or on SNMP errors.
	"""
	try:
		from pysnmp.hlapi import (
			SnmpEngine,
			CommunityData,
			UdpTransportTarget,
			ContextData,
			ObjectType,
			ObjectIdentity,
			getCmd,
		)
	except Exception as exc:  # pragma: no cover - runtime import check
		raise RuntimeError("pysnmp is required for SNMP operations") from exc

	iterator = getCmd(
		SnmpEngine(),
		CommunityData(community, mpModel=1),  # SNMPv2c
		UdpTransportTarget((ip, 161), timeout=timeout, retries=0),
		ContextData(),
		ObjectType(ObjectIdentity(oid)),
	)

	errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
	if errorIndication:
		raise RuntimeError(f"SNMP error: {errorIndication}")
	if errorStatus:
		raise RuntimeError(f"SNMP error: {errorStatus.prettyPrint()}")

	for vb_oid, vb_val in varBinds:
		return str(vb_oid), str(vb_val)

	return None


def snmp_walk(ip: str, oid: str, community: str = DEFAULT_SNMP_COMMUNITY, timeout: int = 2) -> List[Tuple[str, str]]:
	"""Walk an OID subtree via SNMPv2c and return list of (oid, value).

	Raises RuntimeError when pysnmp is not available or on SNMP errors.
	"""
	try:
		from pysnmp.hlapi import (
			SnmpEngine,
			CommunityData,
			UdpTransportTarget,
			ContextData,
			ObjectType,
			ObjectIdentity,
			nextCmd,
		)
	except Exception as exc:  # pragma: no cover - runtime import check
		raise RuntimeError("pysnmp is required for SNMP operations") from exc

	results: List[Tuple[str, str]] = []
	for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(
		SnmpEngine(),
		CommunityData(community, mpModel=1),
		UdpTransportTarget((ip, 161), timeout=timeout, retries=0),
		ContextData(),
		ObjectType(ObjectIdentity(oid)),
		lexicographicMode=False,
	):
		if errorIndication:
			raise RuntimeError(f"SNMP error: {errorIndication}")
		if errorStatus:
			raise RuntimeError(f"SNMP error: {errorStatus.prettyPrint()}")

		for varBind in varBinds:
			results.append((str(varBind[0]), str(varBind[1])))

	return results


def main(argv: List[str]) -> int:
	parser = argparse.ArgumentParser(description="Check network printer reachability and (optionally) query SNMP information")
	parser.add_argument("--ip", required=False, default="10.24.10.12", help="Printer IP address")
	parser.add_argument("--community", required=False, default=DEFAULT_SNMP_COMMUNITY, help="SNMP community (v2c)")
	parser.add_argument("--no-snmp", action="store_true", help="Do not perform SNMP queries; only test TCP reachability")
	parser.add_argument("--max-walk", type=int, default=50, help="Maximum number of SNMP walk lines to print")
	parser.add_argument("--timeout", type=float, default=2.0, help="SNMP/TCP timeout in seconds")
	args = parser.parse_args(argv)

	ip = args.ip
	community = args.community

	print(f"Checking printer at {ip}")

	reachable = check_tcp_port(ip, timeout=args.timeout)
	print(f"Port 9100 reachable: {reachable}")

	if args.no_snmp:
		return 0

	if not pysnmp_available():
		print("pysnmp is not installed in this environment. To enable SNMP queries run:")
		print("  python -m pip install pysnmp")
		return 0

	try:
		print("\nBasic SNMP information:")
		for oid in ("1.3.6.1.2.1.1.1.0", "1.3.6.1.2.1.1.5.0"):
			try:
				got = snmp_get(ip, oid, community, timeout=int(args.timeout))
				print(f" {oid} -> {got[1] if got else 'N/A'}")
			except Exception as e:
				print(f" {oid} -> error: {e}")

		print("\nWalking Printer-MIB (this may take a few seconds):")
		items = snmp_walk(ip, PRINTER_MIB_OID, community, timeout=int(args.timeout))
		if not items:
			print(" No SNMP data returned for Printer-MIB (check community and SNMP availability)")
		else:
			for oid, val in items[: args.max_walk]:
				print(f" {oid} = {val}")
			if len(items) > args.max_walk:
				print(f" ... ({len(items)} total OIDs walked). Increase --max-walk to print more.")

	except Exception as exc:
		print(f"SNMP error: {exc}")

	return 0


if __name__ == "__main__":
	raise SystemExit(main(sys.argv[1:]))

