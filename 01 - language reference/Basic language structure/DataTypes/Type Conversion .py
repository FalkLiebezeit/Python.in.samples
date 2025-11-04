"""Demonstration of type conversion in Python."""

# Define variables of different types
age = 25          # Integer variable
NAME = "ABC"      # String variable
HEIGHT = 5.9      # Float variable

# Convert integer to string
str_age = str(age)
print("Age in string form is:", str_age)

# Convert float to string
str_height = str(HEIGHT)
print("Height in string form is:", str_height)

# Convert string to integer (if possible)
str_num = "42"
int_num = int(str_num)
print("String '42' converted to integer:", int_num)

# Convert string to float (if possible)
str_float = "3.14"
float_num = float(str_float)
print("String '3.14' converted to float:", float_num)