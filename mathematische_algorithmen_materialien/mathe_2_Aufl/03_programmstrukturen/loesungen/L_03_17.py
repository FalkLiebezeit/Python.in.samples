#L_03_17.py
#pascalsche Dreieck
#Fakultaet
def fak(n):
    if n==0:
        return 1
    else:
        return n*fak(n-1)
#Binaerkoeffizient
def binK(n,k):
    return int(fak(n)/(fak(k)*fak(n-k)))  
#pascalsche Dreieck mit Binominalkoeffizient
def pascal(n):
    for n in range(n):
        print() #neue Zeile
        for k in range(n+1):
            print(binK(n,k),end=' ')#Zeilenumbruch verhindern
#Funktionsaufrufe
pascal(11)
#binK(49,6)
