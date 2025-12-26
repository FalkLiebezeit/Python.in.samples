#!/usr/bin/env python

import socket

with socket.create_server(("", 50000)) as s:
    s.listen(1)
    while True:
        komm, addr = s.accept()
        while data := komm.recv(1024):
            print("[{}] {}".format(addr[0], data.decode()))
            nachricht = input("Antwort: ")
            komm.send(nachricht.encode())
        komm.close()
