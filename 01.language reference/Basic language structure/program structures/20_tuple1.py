#18_tuple1.py
t1=(1,2,3)
t2= 4,5,6
t3=t1+t2
t4=3*t2
print("Tupel1 enthält die Elemente:",t1)
print("Tupel2 enthält die Elemente:",t2)
print("Tupel3 enthält die Elemente:",t3)
print("Tupel4 enthält die Elemente:",t4)
print("Das dritte Objekt von t3 hat den Wert:", t3[2])
print("Sind t1 und t2 gleich?",t1==t2)
print("t3 gehört zur Klasse:",type(t3))
print("t1    hat die id",(id(t1)))
print("t1[0] hat die id",(id(t1[0])))
print("t1[1] hat die id",(id(t1[1])))
print("t1[2] hat die id",(id(t1[2])))