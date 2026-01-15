#L_05_05.py
#Heronalgorithmus für Kubikwurzeln
def kubikwurzel(z,n=10):       
    a=z//3  #Startwert
    b=1  
    i=0
    while i<n:
        a=(a+b)/2
        b=(b+z/(a*b))/2
        i=i+1
    return a
z1=27
print("Die Kubikwurzel von",z1,"ist")
print(kubikwurzel(z1))
print(z1**(1/3),"genau")