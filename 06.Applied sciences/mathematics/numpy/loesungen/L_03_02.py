#L_03_02.py
#Kettenschaltung aus 3 Spannungsteilern
import numpy as np
R =1
U2=1
I2=0
R1=R2=R
#Längswiderstand
A1=np.array([[1., R1],
             [0,  1.]])
#Querwiderstand
A2=np.array([[1.,     0],
             [1./R2, 1.]])
A12=A1@A2      #ein Spannungsteiler
A=A12@A12@A12  #drei Spannungsteiler
b=np.array([[U2],[I2]])
E=A@b
print("Kettenform A\n",A)
print("Eingangsgrößen\n",E)
print("Eingangsspannung U1=%3.2f V" %E[0])
print("Eingangsstrom    I1=%3.2f A" %E[1])

