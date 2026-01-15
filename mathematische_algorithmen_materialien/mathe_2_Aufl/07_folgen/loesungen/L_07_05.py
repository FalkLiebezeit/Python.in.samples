from sympy import *
n=symbols('n')
n=2
strF="Die Folge ist "
def a(n):
    #return 2*n
    #return 1/n
    return n/(n+1)
#    
if a(n+1)>a(n):
    print(strF+"streng monoton steigend.")
#    
elif a(n+1)<a(n):
    print(strF+"streng monoton fallend.")
#
else:
    print(strF+"weder monoton steigend noch fallend.")