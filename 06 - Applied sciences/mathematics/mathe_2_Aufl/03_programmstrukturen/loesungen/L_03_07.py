#L_03_07.py
#Wahrheitstabelle Konjunktion Disjunktion
print("a\tb\tc\tUND\tODER")
for a in (False,True):
    for b in (False,True):
        for c in (False,True):
            y1=a and b and c
            y2=a or b or c
            print(a,b,c,y1,y2,sep='\t')