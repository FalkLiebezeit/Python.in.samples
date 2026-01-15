#L_11_05.py
import simpson as sim
#Polynome
def f(x):
    return x**n
#Stammfunktionen
def F(x,n):
    return x**(n+1)/(n+1)
#
a,b=1,10
print("\tSimpson\t\t\t genau")
for n in range(1,10):
    Ag=F(b,n)-F(a,n) #genau
    As=sim.simpson(f,a,b,100) #Simpson
    E=abs(As-Ag)   #Fehler
    print("%2d %17.6f  %17.6f  %9.6f" %(n,As,Ag,E))