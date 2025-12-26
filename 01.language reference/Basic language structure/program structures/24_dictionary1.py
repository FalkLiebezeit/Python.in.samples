#24_dictionary1.py
l1=["Al","Mg"]
l2=[2.71,1.738]
l12=zip(l1,l2)
m1=dict(l12)
neu={"Ti":4.5}
m1.update(neu)
m2={"Fe":7.85,"V":6.12,"Mn":7.43,"Cr":7.2}
print("Schlüssel der Leichtmetalle:",m1.keys())
print("Dichten der Leichtmetalle:",m1.values())
print("Schlüssel der Schwermetalle:",m2.keys())
print("Dichten der Schwermetalle:",m2.values())
print("Leichtmetalle %s %i Einträge" %(m1,len(m1)))
print("Schwermetalle %s %i Einträge" %(m2,len(m2)))
m2.update(m1)
print("Metalle %s %i Einträge" %(m2,len(m2)))
del m2["V"]
print("Metalle %s %i Einträge" %(m2,len(m2)))
print("Dichte von Chrom: %s kg/dm^3" %(m2["Cr"]))