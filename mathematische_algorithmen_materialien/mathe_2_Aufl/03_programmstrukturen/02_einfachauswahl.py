#02_einfachauswahl.py
from random import random
a=random()
b=0.5
print("\ta\t\tb")
#Fallabfrage
if a > b:
    print(a,">",b)
    print("a ist größer als b")
else:
    print(a,"<",b)
    print("a ist kleiner als b")