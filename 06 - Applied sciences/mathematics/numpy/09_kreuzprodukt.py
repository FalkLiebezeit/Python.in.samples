#07_kreuzprodukt.py
import numpy as np
F=2,7,-3
l=-2,3,4
F_B=np.sqrt(np.dot(F,F))
l_B=np.sqrt(np.dot(l,l))
cos_Fl=np.dot(F,l)/(F_B*l_B)
winkel=np.degrees(np.arccos(cos_Fl))
M=np.cross(F,l)
M_B=np.sqrt(np.dot(M,M))
#Ausgabe
print("Betrag der Kraft       :",F_B,"N")
print("Betrag des Hebelarms   :",l_B,"m")
print("Winkel zwischen F und l:",winkel,"°")
print("Drehmoment M           :",M,"Nm")
print("Betrag des Drehmoments :",M_B,"Nm")
