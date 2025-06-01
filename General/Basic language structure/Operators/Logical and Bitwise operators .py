#Logical and Bitwise operators in Python

A=1
B=0
#"And" operator will check both the conditions i.e.if one condition is true and another is false,then output will be false.
print(A and B)#output will be printed 0 i.e.false
#In "or" operator,one condition is true and another is false,then output will be true.
print(A or B) #output will be printed 1 i.e.true
print(not A)  #output will be "False"
C=int(input("Enter the value"))
print("The value of c is",C)
D=int(input("Enter the value"))
print("The value of d is",D)

#Bitwise AnD(&)operator
print('Result after Bitwise AND operation is',C&D)
#Bitwise or(|) operator
print('Result after Bitwise OR operation is',C|D)
#Bitwise XOR operator
print('Result after Bitwise XOR operation is',C^D)
#Bitwise Right Shift operator
print('Result after Right Shift operation is',C>>1)
#Bitwise Left Shift Operator
print('Result after Left Shift operation is',C<<1)
#Assignment operator
C+=10
print('c value after adding 10 using Assignment operator is',C)
C-=3
print('c value after subtracting 3 using Assignment operator is',C)
