#05_modulo.py
def mod(a,b):
    i=0
    while a>=b:
        a=a-b
        i=i+1
    return i,a
#Hauptprogramm
z1=17
z2=5
ganz,rest=mod(z1,z2)
print(z1,"geteilt durch",z2,"ergibt:",ganz,"Rest",rest)
print("Mit divmod berechnet:",divmod(z1,z2))