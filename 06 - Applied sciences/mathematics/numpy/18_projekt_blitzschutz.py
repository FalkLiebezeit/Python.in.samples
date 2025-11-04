#18_projekt_blitzschutz.py
import numpy as np
Iq=1e5 #Stromstärke in A
g=10
A=50  #Leiterquerschnitt in mm^2
l=10
b=5
h=3
Gh=g*A/h
Gl=g*A/l
Gb=g*A/b
G=np.array([[Gb+Gh+Gl, -Gl, -Gb, 0],
            [-Gl, Gb+Gh+Gl, 0,-Gb],
            [-Gb, 0, Gb+Gh+Gl,-Gl],
            [ 0,-Gb,-Gl, Gb+Gh+Gl]])
I=np.array([Iq,0,0,0])
U=np.linalg.solve(G,I)
I10=U[0]*Gh
I20=U[1]*Gh
I30=U[2]*Gh
I40=U[3]*Gh
I12=(U[0]-U[1])*Gl
I13=(U[0]-U[2])*Gb
I34=(U[2]-U[3])*Gl
I24=(U[1]-U[3])*Gb
print("--Spannungsfälle der Ableitungen--")
print("Spannung U10: %3.2f V" %U[0])
print("Spannung U20: %3.2f V" %U[1])
print("Spannung U30: %3.2f V" %U[2])
print("Spannung U40: %3.2f V" %U[3])
print("--Stromstärken in den Ableitungen--")
print("Stromstärke I10: %3.2f A" %I10)
print("Stromstärke I20: %3.2f A" %I20)
print("Stromstärke I30: %3.2f A" %I30)
print("Stromstärke I40: %3.2f A" %I40)
print("--Stromstärken in den Fangleitungen--")
print("Stromstärke I12: %3.2f A" %I12)
print("Stromstärke I13: %3.2f A" %I13)
print("Stromstärke I34: %3.2f A" %I34)
print("Stromstärke I24: %3.2f A" %I24)

