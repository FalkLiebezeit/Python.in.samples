#12_sympy_lgs2.py
from sympy import symbols,Matrix,linsolve
x1,x2,x3=symbols('x1,x2,x3')
A=Matrix([[3,2,1],
          [1,2,3],
          [2,1,4]])
b=Matrix([10,14,16])
inverse=A.inv() #A**-1 
L1=inverse*b
L2=A.gauss_jordan_solve(b)
L3=linsolve([A,b],(x1,x2,x3))
#Ausgaben
print("Inverse von A\n",inverse)
print("Lösung mit Inverse\n",L1)
print("x1 = %3.3f\nx2 = %3.3f\nx3 = %3.3f"%\
      (L1[0],L1[1],L1[2]))
print("Lösung mit gauss_jordan_solve\n",L2)
print("x1 = %3.3f\nx2 = %3.3f\nx3 = %3.3f"%\
      (L2[0][0],L2[0][1],L2[0][2]))
print("Lösung mit linsolve\n",L3)
print("x1 = %3.3f\nx2 = %3.3f\nx3 = %3.3f"%\
      (L3.args[0][0],L3.args[0][1],L3.args[0][2]))


