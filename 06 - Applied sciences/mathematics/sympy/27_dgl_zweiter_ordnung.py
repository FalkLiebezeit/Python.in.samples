#27_dgl_zweiter_ordnung.py
from sympy import *
t=symbols("t")
u=Function("f")(t)
U1=10
R1,L1,C1=5/2,1,1
R2,L2,C2=2,1,1
R3,L3,C3=2,1/2,1/4
#DGL 2. Ordnung
dgl1=L1*C1*Derivative(u,t,t)+R1*C1*Derivative(u,t)+u-U1
dgl2=L2*C2*Derivative(u,t,t)+R2*C2*Derivative(u,t)+u-U1
dgl3=L3*C3*Derivative(u,t,t)+R3*C3*Derivative(u,t)+u-U1
#Lösung der DGL
L1=dsolve(dgl1,u)
L2=dsolve(dgl2,u)
L3=dsolve(dgl3,u)
#Ausgabe der Lösung
print(L1,"\n",L2,"\n",L3)

