# -*- coding: utf-8 -*-
"""Comparison operators

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zhHEXIxnix8wfp7I3SdZHNibbgTtJSzs
"""

#Input two numbers from the user

num1= float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Perform comparison operations

equal = num1 == num2

note_qual = num1 != num2
greater_than = num1 > num2

less_than = num1 < num2

greater_than_or_equal = num1 >= num2
less_than_or_equal = num1 < num2

#Display the results

print("Equal:", equal)

print("Not Equal:", note_qual)

print("Greater Than:", greater_than)
print("Less Than:", less_than)

print("Greater Than or Equal:", greater_than_or_equal)
print("Less Than or Equal:", less_than_or_equal)