#19_for_for_schleife3.py
b=5   #Breite in cm
h=10  #Höhe in  cm
y1,y2=-b/2,b/2 #Grenzen der y-Achse
z1,z2=-h/2,h/2 #Grenzen der z-Achse
#Funktionsdefinition
def f(y,z):
    return z**2
#Zweifachintegral berechnen
dy=dz=1e-2
m=int((z2-z1)/dz) #Höhe
n=int((y2-y1)/dy) #Breite
sz=0
for i in range(m):    #außen
    z=z1+i*dz
    sy=0
    for j in range(n): #innen
        y=y1+j*dy
        sy=sy+f(y,z)
    sz=sz+sy
Iy=sz*dy*dz
#Ausgabe
print("Flächenmoment für ein Rechteckquerschnitt")
print("Iy =",Iy, "cm^4")
print("Iy =",b*h**3/12,"cm^4 genau")
print(m,n)