#15_mulmatrix4.py
import numpy as np
x=1
y=0
z=0
wx=0
wy=0
wz=1
m=6
w_Z=np.array([wx,wy,wz])
I=m*np.array([[y**2+z**2, -x*y, -x*z],
               [-x*y, x**2+z**2, -y*z],
               [-x*z, -y*z, x**2+y**2]])
w_S=np.array([[wx],
               [wy],
               [wz]])
#Berechnung der Rotationsenergie
Erot=0.5*w_Z@I@w_S
#Erot=0.5*w_S.T@I@w_S
#Ausgabe
print("Rotationsenergie: %3.2f Joule" %Erot)


