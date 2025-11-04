#L_02_05.py
#ggt
def ggT(a, b):
    while b != 0:
        a, b = b, a % b
    return a

z1=90
z2=6
t=ggT(z1,z2)
print("Größte gemeinsamer Teiler von %i und %i ist %i" %(z1,z2,t))

