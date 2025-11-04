"""Demonstration of tuple creation, access, and immutability in Python."""

# Create a tuple using parentheses
new_tuple1 = (10, 20, 30, 40, 50)
print("Tuple 1:", new_tuple1)
print("Type of Tuple 1:", type(new_tuple1))

# Access the 2nd element of the tuple (index 1)
print("Second element of Tuple 1:", new_tuple1[1])

# Create a tuple using the tuple() constructor
new_tuple2 = tuple((11, 22, 33, 44, 55))
print("Tuple 2:", new_tuple2)

# Attempting to modify an element of a tuple will raise a TypeError
try:
    new_tuple1[1] = 29
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable and do not support item assignment.")