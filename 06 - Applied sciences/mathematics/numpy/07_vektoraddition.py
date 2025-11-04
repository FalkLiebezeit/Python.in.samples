#07_vektoraddition.py
import numpy as np
F1=-6,4
F2=4,-8
F3=4,2
F1=np.array(F1)
F2=np.array(F2)
F3=np.array(F3)
Fres=F1+F2+F3
F_1=np.sqrt(F1[0]**2+F1[1]**2)
F_2=np.sqrt(F2[0]**2+F2[1]**2)
F_3=np.sqrt(F3[0]**2+F3[1]**2)
F_res=np.sqrt(Fres[0]**2+Fres[1]**2)
winkel=np.arctan(Fres[0]/Fres[1])
winkel=np.degrees(winkel)
#Ausgabe
print("Koordinaten von F1:",F1)
print("Koordinaten von F2:",F2)
print("Koordinaten von F3:",F3)
print("Betrag von F1     :",F_1)
print("Betrag von F2     :",F_2)
print("Betrag von F3     :",F_3)
print("resultierend Kraft:",Fres)
print("Betrag von Fres   :",F_res)
print("Winkel von Fres   :",winkel,"°")
