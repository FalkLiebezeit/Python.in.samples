C = int(input("Enter  the value"))
print ("The value of c is",C)
D = int(input("Enter  the value"))
print("The value of d is",D)

lst1=[12,3,5,6,9] #A list is created and the elements are placed into it.

if C in lst1:
   print('c value is available in the list',C in lst1)
else:
   print('c value is not available in the list',C in lst1)
if D not in lst1:
 print('d value is not available in the list',D not in lst1)
else:
 print('d value is available in the list',D not in lst1)
