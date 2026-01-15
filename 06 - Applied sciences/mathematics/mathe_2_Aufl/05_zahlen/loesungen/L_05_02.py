#L_05_03.py
#Neunerprüfung
def Q(z):
    strZahl=str(z)
    n=len(strZahl)
    qs=0
    for ziffer in strZahl:
        qs=qs+int(ziffer)
    return qs

a=463
b=527
c=a*b
print("a =",a,", Q(a) =",Q(a))
print("b =",b,", Q(b) =",Q(b))
print("a*b =",c)
print("Q(a*b) =",Q(a*b), ", Q(a)*Q(b) =",Q(a)*Q(b))
print("Q(a)*Q(b) - Q(a*b) =",Q(a)*Q(b)-Q(a*b))
print("Lässt sich",Q(a)*Q(b)-Q(a*b),"durch 9 teilen?")
print((Q(a)*Q(b)-Q(a*b)),"mod 9 =",(Q(a)*Q(b)-Q(a*b))%9)
