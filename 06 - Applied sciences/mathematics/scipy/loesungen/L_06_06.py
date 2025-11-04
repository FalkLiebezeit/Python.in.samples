#L_06_06.py
#Doppeltintegral
import scipy.integrate as integral
#Stromdichte
def J(y,x):
    return x**2*y
    
a=4
b=2
#Stromstärke
I=integral.dblquad(J,0,a,0,b)[0]
print("Stromstärke:",I,"A")
