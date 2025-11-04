#L_08_02.py
#Stern-Dreieck-Umwandlung
import numpy as np
Z10=10+5j
Z20=8-14j
Z30=14+10j
#Berechnung
Z12=Z10+Z20+Z10*Z20/Z30
Z23=Z20+Z30+Z20*Z30/Z10
Z31=Z10+Z30+Z10*Z30/Z20
#Ausgabe
print("Z12",Z12)
print("Z23",Z23)
print("Z31",Z31)


