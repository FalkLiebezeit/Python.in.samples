#!/usr/bin/env python

geheimnis = 1337
while (versuch := int(input("Raten Sie: "))) != geheimnis:
    if versuch == 0:
        print("Das Spiel wird beendet")
        break
    elif versuch < geheimnis:
        print("Zu klein")
    elif versuch > geheimnis:
        print("Zu groß")
else:
    print("Sie haben es geschafft!")
