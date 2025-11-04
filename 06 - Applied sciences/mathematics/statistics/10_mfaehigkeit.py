#10_mfaehigkeit.py
import numpy as np
sollwert=50
To=5
Tu=-5
T=To-Tu
werte = np.loadtxt("./DataInput/daten.txt")
m=np.mean(werte)
s=np.std(werte,ddof=1)
Cm=T/(6*s)
OGW=sollwert+To
UGW=sollwert+Tu
delta_o=OGW-m
delta_u=m-UGW
if delta_o > delta_u:
    delta_k=delta_u
else:
    delta_k=delta_o
Cmk=delta_k/(3*s)
print("Mittelwert:",m)
print("Standardabweichung:",s)
print("Maschinenfähigkeitsindex:  ",Cm)
print("Maschinenfähigkeitkennwert:",Cmk)

