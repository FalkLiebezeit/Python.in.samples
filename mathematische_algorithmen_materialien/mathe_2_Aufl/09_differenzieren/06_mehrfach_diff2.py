#06_mehrfach_diff2.py
#Funktionsdefinition
def f(x):
    return x**4/32
#zentraler Differenzenquotient
def diff(f,h=1e-3):
    return lambda x:(f(x+h)-f(x-h))/(2*h)
#Ableitungen
x0=2
y1=diff(f)
y2=diff(diff(f))
y3=diff(diff(diff(f)))
y4=diff(diff(diff(diff(f))))
#Ausgaben
print(y1(x0))
print(y2(x0))
print(y3(x0))
print(y4(x0))

