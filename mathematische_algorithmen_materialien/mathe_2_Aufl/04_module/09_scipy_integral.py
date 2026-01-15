#09_scipy_integral.py
from scipy.optimize import newton
from scipy.integrate import quad
def f(x):
    return -x**2+5*x-3
#Nullstelle berechnen
x01,x02=newton(f,[0.6,4.2])
A=quad(f,x01,x02)#[0]
#Ausgabe
print("Nullstellen:  ",x01,x02)
print("Flächeninhalt:",A)

