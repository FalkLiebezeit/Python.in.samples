#L02_04.py
#Heron
a=2.
x=a
i=0
while i<2000:
    x=(x+a/x)/2
    i=i+1
print(x)