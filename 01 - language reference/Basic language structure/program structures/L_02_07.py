#L_02_07.py
'''Zweifachintegral'''
x1,x2=0,2 #Grenzen der x-Achse
y1,y2=0,1 #Grenzen der y-Achse
n=200
#Funktionsdefinition
def f(x,y):
    return 5-y-x
#Zweifachintegral berechnen
n=200
dx=(x2-x1)/n
dy=(y2-y1)/n
sy=0
for i in range(n):
    y=y1+i*dy+dy/2
    sx=0
    for j in range(n):
        x=x1+j*dx+dx/2
        sx=sx+f(x,y)
    sy=sy+sx
V=sy*dx*dy
#Ausgabe
print("V =",V)
#Lösung mit SciPy
from scipy.integrate import dblquad
V=dblquad(f,x1,x2,y1,y2)[0]
print("V =",V,"dblquad")






