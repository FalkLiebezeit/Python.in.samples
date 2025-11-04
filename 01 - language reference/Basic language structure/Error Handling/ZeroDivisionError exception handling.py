# Demonstration of ZeroDivisionError exception handling in Python

try:
    # Prompt user for input and convert to integer
    output = int(input("Enter a number: "))
    # Attempt to divide by zero (will raise ZeroDivisionError)
    output1 = output / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")