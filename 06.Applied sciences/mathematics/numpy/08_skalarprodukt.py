#06_skalarprodukt.py
import numpy as np
F=2,7,-3
s=-2,3,4
F_B=np.sqrt(np.dot(F,F))
s_B=np.sqrt(np.dot(s,s))
cos_Fs=np.dot(F,s)/(F_B*s_B)
winkel=np.degrees(np.arccos(cos_Fs))
W=np.dot(F,s)
#Ausgabe
print("Betrag der Kraft:",F_B,"N")
print("Betrag des Weges:",s_B,"m")
print("Winkel zwischen F und s:",winkel,"°")
print("Arbeit:",W,"Nm")
