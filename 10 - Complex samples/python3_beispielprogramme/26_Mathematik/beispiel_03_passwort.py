#!/usr/bin/env python

import hashlib

pwhash = "578127b714de227824ab105689da0ed2"

m = hashlib.md5(input("Ihr Passwort bitte: ").encode("utf-8"))
if pwhash == m.hexdigest():
    print("Zugriff erlaubt")
else:
    print("Zugriff verweigert")

