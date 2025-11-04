#25_dictionary2.py
e=["unique","statement","assignment","loop","parentheses"]
d=["eindeutig","Anweisung","Zuweisung","Schleife","Klammern"]
e2d=dict(zip(e,d))
d2e=dict(zip(d,e))
print("statement:", e2d["statement"])
print("Schleife:", d2e["Schleife"])