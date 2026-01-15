#L_07_03.py
def fib(n):
    a1,a2=0,1
    for i in range(n+1):
        a1,a2=a2,a1+a2
        print(a1,end=" ")

fib(10)   

    
