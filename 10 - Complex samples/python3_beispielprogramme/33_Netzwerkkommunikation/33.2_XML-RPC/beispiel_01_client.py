#!/usr/bin/env python

from xmlrpc.client import ServerProxy

cli = ServerProxy("http://127.0.0.1:50000")

print(cli.fak(5))
print(cli.quad(5))

