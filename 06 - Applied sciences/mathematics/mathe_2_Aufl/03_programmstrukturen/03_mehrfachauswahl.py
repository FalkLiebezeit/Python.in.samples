#05_mehrfachauswahl.py
from random import randint
a=randint(1,6)
#Fallabfragen
if a==1:
    print("Es wurde eine 1 gewürfelt")
elif a==2:
    print("Es wurde eine 2 gewürfelt")
elif a==3:
    print("Es wurde eine 3 gewürfelt")
elif a==4:
    print("Es wurde eine 4 gewürfelt")
elif a==5:
    print("Es wurde eine 5 gewürfelt")
elif a==6:
    print("Es wurde eine 6 gewürfelt")
else:
    print("Fehler")