# Check for Boolean True/False in Expressions
# Comparisons always return a Boolean value (True or False)
print(100 > 200)  # False: 100 is not greater than 200
print(100 == 200)  # False: 100 is not equal to 200
print(100 < 200)  # True: 100 is less than 200

# Check for Boolean True/False in different values of variables
a = "Python"  
b = 50  

# The bool() function converts values to their Boolean equivalent
print(bool(a))  # True: Non-empty string evaluates to True
print(bool(b))  # True: Non-zero number evaluates to True
print(bool(0))  # False: Zero evaluates to False
print(bool(-10))  # True: Any non-zero number, even negative, is True
print(bool(["January", "February", "March", "April"]))  # True: Non-empty list is True
print(bool(True))  # True: Explicit Boolean value True
print(bool(False))  # False: Explicit Boolean value False
print(bool(None))  # False: None evaluates to False
print(bool(""))  # False: Empty string evaluates to False
print(bool(()))  # False: Empty tuple evaluates to False
print(bool([]))  # False: Empty list evaluates to False
print(bool({}))  # False: Empty dictionary evaluates to False