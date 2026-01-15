#L_05_01.py
#gerade- und ungerade Zahlen
def gerade_ungerade(z):
    if z%2==0:
        return "gerade"
    else:
        return "ungerade"
    
zahl=2349
print("Die Zahl",zahl,"ist",gerade_ungerade(zahl))
    