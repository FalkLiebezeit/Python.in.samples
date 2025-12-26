#26_dgl_erster_ordnung.py
from sympy import *
t=symbols("t")
u=Function("f")(t)
R,C=1,2
U0=10
tau=R*C
#DGL 1. Ordnung
dgl1=tau*Derivative(u,t)+u
dgl2=tau*Derivative(u,t)+u-U0
dgl3=tau*Derivative(u,t)+u-U0*t
dgl4=tau*Derivative(u,t)+u-U0*exp(t)
dgl5=tau*Derivative(u,t)+u-U0*sin(t)
#Lösung der DGL
L1=dsolve(dgl1,u)
L2=dsolve(dgl2,u)
L3=simplify(dsolve(dgl3,u))
L4=dsolve(dgl4,u)
L5=simplify(dsolve(dgl5,u))
#Ausgabe der Lösung
print(L1,"\n",L2,"\n",L3,"\n",L4,"\n",L5)

