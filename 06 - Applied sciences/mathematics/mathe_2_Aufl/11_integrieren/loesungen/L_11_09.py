#L_11_09.py
#Zweifachintegral
from scipy.integrate import dblquad
#
def f(x,y):
    z=100-6*x**2*y
    return z
#Grenzen der x-Achse
x1,x2=0,2
#Grenzen der y-Achse
y1,y2=-1,1
V = dblquad(f,y1,y2,x1,x2)[0]
print("Volumen:",V)


