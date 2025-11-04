#26_sets.py
menge1={"A","B","C","D"}
menge2={"C","D","E","F"}
schnittmenge= menge1 & menge2
differenz=menge1 - menge2
vereinigung=menge1 | menge2
print("menge1:",menge1)
print("menge2:",menge2)
print("Schnittmenge:",schnittmenge)
print("Differenzmenge:",differenz)
print("Vereinigungsmenge:",vereinigung)
print("Ist B in menge1 enthalten?", menge1.issuperset("B"))