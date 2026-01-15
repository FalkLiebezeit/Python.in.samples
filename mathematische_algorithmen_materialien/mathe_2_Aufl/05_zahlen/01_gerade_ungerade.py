#03_gerade_ungerade.py
def gerade_ungerade(zahl):
    strZahl=str(zahl)
    letzteZiffer=strZahl[-1]
    lz=int(letzteZiffer)
    if (lz==0) or (lz==2) or (lz==4) or (lz==6) or (lz==8):
        return "gerade Zahl"
    else:
        return "ungerade Zahl"
#Hauptprogramm
#z=1234
z=234563
print(z,"ist eine",gerade_ungerade(z))
