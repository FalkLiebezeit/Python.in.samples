#09_for_wahrheitstabelle.py
print("Logische Verknüpfungen")
print("a\tb\tUND\tODER")
for a in (False,True):
    for b in (False,True):
        y1=a and b
        y2=a or b
        print(a,b,y1,y2,sep='\t')