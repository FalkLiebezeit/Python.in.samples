#08_integral_vergleich.py
import scipy.integrate as integral

def f(x):
    return x**2
#Rechtecksummen
def rect(f,a,b,h=1e-6):
    n=int((b-a)/h)
    s=0
    for k in range(1,n):
        x=a+k*h
        s=s+f(x)
    return s*h

a=0 #untere Grenze
b=2 #obere Grenze
A1=rect(f,a,b)
A2=integral.quad(f,a,b)#[0]
A3=integral.fixed_quad(f,a,b,n=4)#[0]
A4=integral.quadrature(f,a,b,tol=1e-6)#[0]
A5=integral.romberg(f,a,b,tol=1e-6,show=False)
#Ausgaben
print("Rechtecksummen\t: ",A1)
print("quad\t\t:",A2)
print("fixed_quad\t:",A3)
print("quadrature\t:",A4)
print("romberg\t\t: ",A5)