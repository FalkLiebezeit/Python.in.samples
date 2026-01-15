#07_euklid.py
a=174
b=78
while a!=b:
    if a>b:
        print(a,"-",b,"=",a-b)
        a=a-b
    elif b>a:
        print(b,"-",a,"=",b-a)
        b=b-a
    