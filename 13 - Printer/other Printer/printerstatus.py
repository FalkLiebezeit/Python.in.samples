"""
Printer status checker for a network Canon MF754Cdw.

Features:
- TCP port check (port 9100) to test reachability
- SNMP v2c queries (default community: 'public') for basic info and Printer-MIB walk

Usage:
	python printerstatus.py --ip 10.24.10.12

If `pysnmp` is not installed, install it into your project's venv:
	C:/path/to/venv/Scripts/python.exe -m pip install pysnmp

The script prints discovered SNMP OIDs and their values so you can locate
the exact Printer-MIB OIDs that correspond to the printer state on your device.
"""

from __future__ import annotations
import argparse
import socket
import sys
from typing import List, Tuple

DEFAULT_SNMP_COMMUNITY = "public"
PRINTER_MIB_OID = "1.3.6.1.2.1.43"  # Printer-MIB base OID


def check_tcp_port(ip: str, port: int = 9100, timeout: float = 2.0) -> bool:
	"""Check if TCP port on the printer is reachable.

	Returns True if connection succeeded, False otherwise.
	"""
	try:
		with socket.create_connection((ip, port), timeout=timeout):
			return True
	except Exception:
		return False


def try_import_pysnmp() -> bool:
	try:
		# do a lazy import so script can still show reachability without pysnmp
		import pysnmp  # noqa: F401
		return True
	except Exception:
		return False


def snmp_get(ip: str, oid: str, community: str = DEFAULT_SNMP_COMMUNITY, timeout: int = 2):
	"""Perform a SNMPv2c GET for a single OID and return (oid, value) or None.
	Requires `pysnmp`.
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
	except Exception as exc:
		raise RuntimeError("pysnmp is required for SNMP operations") from exc

	iterator = getCmd(
		SnmpEngine(),
		CommunityData(community, mpModel=1),  # v2c
		UdpTransportTarget((ip, 161), timeout=timeout, retries=0),
		ContextData(),
		ObjectType(ObjectIdentity(oid)),
	)

	errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
	if errorIndication:
		raise RuntimeError(f"SNMP error: {errorIndication}")
	if errorStatus:
		raise RuntimeError(f"SNMP error: {errorStatus.prettyPrint()}")

	# return first varBind
	for oid, val in varBinds:
		return str(oid), str(val)

	return None


def snmp_walk(ip: str, oid: str, community: str = DEFAULT_SNMP_COMMUNITY, timeout: int = 2) -> List[Tuple[str, str]]:
	"""Perform a SNMPv2c walk starting at `oid` and return list of (oid, value).
	Requires `pysnmp`.
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
	except Exception as exc:
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
	parser = argparse.ArgumentParser(description="Check status of a network printer via TCP and SNMP")
	parser.add_argument("--ip", required=False, default="10.24.10.12", help="Printer IP address")
	parser.add_argument("--community", required=False, default=DEFAULT_SNMP_COMMUNITY, help="SNMP community (v2c)")
	parser.add_argument("--no-snmp", action="store_true", help="Skip SNMP queries and only test reachability")
	args = parser.parse_args(argv)

	ip = args.ip
	community = args.community

	print(f"Checking printer at {ip}")

	reachable = check_tcp_port(ip)
	print(f"Port 9100 reachable: {reachable}")

	if args.no_snmp:
		return 0

	if not try_import_pysnmp():
		print("pysnmp package is not installed. To enable SNMP queries, install it into your venv:")
		print("  python -m pip install pysnmp")
		return 0

	# Try read some useful OIDs
	try:
		print("\nBasic SNMP info:")
		for oid in ("1.3.6.1.2.1.1.1.0", "1.3.6.1.2.1.1.5.0",):
			try:
				got = snmp_get(ip, oid, community)
				print(f" {oid} -> {got[1] if got else 'N/A'}")
			except Exception as e:
				print(f" {oid} -> error: {e}")

		print("\nWalking Printer-MIB (this may take a few seconds):")
		items = snmp_walk(ip, PRINTER_MIB_OID, community)
		if not items:
			print(" No SNMP data returned for Printer-MIB (check community and SNMP availability)")
		else:
			# Print a subset first, then full list
			for oid, val in items[:50]:
				print(f" {oid} = {val}")
			if len(items) > 50:
				print(f" ... ({len(items)} total OIDs walked)\nYou can increase the printed count in the script if you need more.")

	except Exception as exc:
		print(f"SNMP error: {exc}")

	return 0


if __name__ == "__main__":
	raise SystemExit(main(sys.argv[1:]))

