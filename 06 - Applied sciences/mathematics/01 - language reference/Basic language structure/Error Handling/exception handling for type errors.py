import sys

# Demonstration of exception handling for type errors in Python
try:
    a = 5
    b = 'ABC'
    # Attempting to add an integer and a string will raise a TypeError
    c = a + b
except TypeError:
    print('Caught TypeError: Cannot add int and str')