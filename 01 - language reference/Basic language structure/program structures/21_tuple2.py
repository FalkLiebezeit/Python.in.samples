#21_tuple2.py
a,b=10,20
t=(a,b)
print("----vorher----")
print("Wert von a=%i id von a=%i" %(a,id(a)))
print("Wert von b=%i id von b=%i" %(b,id(b)))
print("Wert von t=",t,"id von t=",id(t))
a,b=b,a
print("----nachher----")
print("Wert von a=%i id von a=%i" %(a,id(a)))
print("Wert von b=%i id von b=%i" %(b,id(b)))
print("Wert von t=",t,"id von t=",id(t))
