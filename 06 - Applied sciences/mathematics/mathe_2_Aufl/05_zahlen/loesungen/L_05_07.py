#L_05_07.py
#π-Berechnung nach Bailly 1995
from math import pi
n=11
pib=0
for k in range(0,n):
    pib=pib+(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))/16**k
print("Bailly:",pib)
print("genau :",pi) #15 Stellen Genauigkeit
