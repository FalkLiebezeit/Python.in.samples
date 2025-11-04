#!/usr/bin/env python

import re

with open("rheinwerk-verlag.html", "r") as f:
    html = f.read()

it = re.finditer(r"""
    <a\ .*?             # Achtung: Leerzeichen nach a benötigt Backslash
        href=[\"\']     # Doppelte oder einfache Anführungszeichen
                        # umschließen das Ziel des Links
                 (.*?)  # Wir erlauben beliebige Zeichen im Linkziel ...
             [\"\']
    .*?>
        (.*?)           # ... genauso wie im Linktext
    </a>
""", html, re.I | re.VERBOSE)

for n, m in enumerate(it):
    print("#{} Name: {}, Link: {}".format(n, m.group(2), m.group(1)))
