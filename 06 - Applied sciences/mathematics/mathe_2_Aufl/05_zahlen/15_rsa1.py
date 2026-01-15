#15_rsa1.py
from sympy import mod_inverse,igcd
#Empfänger B
p,q=53,97            #1.Schritt: zwei Primzahlen bestimmen
n=p*q                #2.Schritt: Modul berechnen
phi=(p-1)*(q-1)      #3.Schritt: eulersche Funktion berechnen
e=101                #4.Schritt: öffentlichen Schlüssel wählen
d=mod_inverse(e,phi) #5.Schritt: geheimen Schlüssel berechnen
#Sender A
m=2525   #Nachricht
c=m**e%n #verschlüsseln
#Empfänger B
m=c**d%n #entschlüsseln
#Ausgaben
print("öffentliche Schlüssel e =",e,", n =",n)
print("phi =",phi)
print("privater Schlüssel d =",d)
print("Nachricht:",m)
print("verschlüsselte Nachricht:",c)
print("entschlüsselte Nachricht:",m)
print("ggT(m,n) =",igcd(m,n))

# print((m**e%n)**d%n)
# print(m**(e*d)%n)