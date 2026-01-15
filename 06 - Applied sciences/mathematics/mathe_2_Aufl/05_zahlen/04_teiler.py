#06_teiler.py
def berechneTeiler(zahl):
    teiler=[]
    for t in range(2,zahl//2+1):
        if zahl%t==0:
            teiler.append(t)
        else:
            continue
    return teiler
#Hauptprogramm
z1=78
z2=174
print("Teiler von",z1,"=",berechneTeiler(z1))
print("Teiler von",z2,"=",berechneTeiler(z2))
