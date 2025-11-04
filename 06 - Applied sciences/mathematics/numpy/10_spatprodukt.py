#08_spatprodukt.py
import numpy as np
a=2,0,0
b=0,3,0
c=0,0,4
a_B=np.sqrt(np.dot(a,a))
b_B=np.sqrt(np.dot(b,b))
c_B=np.sqrt(np.dot(c,c))
V=np.dot(c,np.cross(a,b))

#Ausgabe
print("Betrag von a:",a_B)
print("Betrag von b:",b_B)
print("Betrag von c:",c_B)
print("Spatprodukt :",V)
