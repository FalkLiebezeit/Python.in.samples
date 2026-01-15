#16_rsa2.py
from sympy import prime, mod_inverse
#Empfänger B: Schlüssel erzeugen
def schluessel(): 
    e=47                    
    p,q=prime(50),prime(60) #Primzahlen erzeugen
    phi=(p-1)*(q-1)         #Eulersche phi-Funktion
    d=mod_inverse(e,phi)    #geheimer Schlüssel, decrypt
    txtD=open('schluessel.txt','w')#geheimen Schlüssel speichern
    txtD.write(str(d))
    txtD.close()
    n=p*q
    return e,n #öffentliche Schlüssel
#Sender A: Nachricht verschlüsseln
def verschluesseln():
    m='5234.1562.3398.6976' #Nachricht
    e,n=schluessel()
    c = [(ord(i)**e)%n for i in m]
    return c
#Empfänger B: Nachricht entschlüsseln
def entschluesseln():
    c=verschluesseln()
    n=schluessel()[1]
    txtD=open('schluessel.txt','r').read()
    d=int(txtD)
    mi = [(c[i]**d)%n for i in range(len(c))]
    m=''
    for i in range(len(mi)):
        m=m+chr(mi[i])
    return m
#Hauptprogramm
print("verschlüsselte Nachricht\n",verschluesseln())
print("entschlüsselte Nachricht\n",entschluesseln())
