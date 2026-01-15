#for_dict.py
print("Ableitungen")
ableitungen={'sin(x)':'cos(x)','ln(x)':'1/x','e**x':'e**x'}
for i,j in ableitungen.items():
    print(i,":",j)
print("Stammfunktionen")
integrale={'sin(x)':'-cos(x)','1/x':'ln(x)','e**x':'e**x'}
for i,j in integrale.items():
    print(i,":",j)