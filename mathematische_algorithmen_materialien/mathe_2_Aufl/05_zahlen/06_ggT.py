#06_ggT.py
#Division mit Rest
def ggT(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#Hauptprogramm
z1,z2=78,174
t=ggT(z1,z2)
print("Größte gemeinsamer Teiler von %i und %i ist %i" %(z1,z2,t))

