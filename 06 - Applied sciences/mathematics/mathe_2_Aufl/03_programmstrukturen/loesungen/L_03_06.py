#L_03_06.py
#Wahrheitstabelle Konjunktion Disjunktion
print("a\tb\tUND\tODER")
for a in (False,True):
    for b in (False,True):
        y1=a and b
        y2=a or  b
        print(a,b,y1,y2,sep='\t')