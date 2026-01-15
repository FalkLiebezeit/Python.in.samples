#18_horner_schema.py
#naive Methode
def polynom(a,x):
    n=len(a)
    p=a[0]
    for i in range(1,n):
        p = p + a[i]*x**i
    return p
#Horner-Schema
def horner(a,x):
    n=len(a)-1
    p=a[n]
    for i in range(n-1,-1,-1):
        p = x*p + a[i]
    return p
#Hauptprogramm
z=2
a=[2,1,2,3,4,5]
print("Wert des Polynoms an der Stelle",z)
print(polynom(a,z))
print(horner(a,z))

#print(i,p) #unter Zeile 13 einfügen

'''
#zur Kontrolle
def f(x):
    return  2 + x + 2*x**2 + 3*x**3 + 4*x**4 + 5*x**5
print(f(z))
'''
#a=[1,0,0,0,-2,3]

'''
def evaluate(x, a):
    result = 0
    for i in range(len(a)-1, -1, -1):
        result = a[i] + (x*result)
    return result

# Copyright © 2000–2015, Robert Sedgewick, Kevin Wayne, and Robert Dondero.
# Last updated: Fri Oct 20 20:45:16 EDT 2017.
'''
'''
#eine pythonische Lösung
def horner(b,x):
    p=b[0]
    for a in b[1:]:
        p=p*x + a
    return p
'''