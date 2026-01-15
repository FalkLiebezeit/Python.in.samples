"""Demonstration of list aliasing in Python.

Shows that assigning one list to another variable creates an alias,
so changes to one affect the other.
"""

# Create a list and assign it to another variable (aliasing)
list1 = [1, 2, 3, 4, 5]
list2 = list1  # list2 is an alias for list1

print("Initial list2:", list2)

# Append an element to list1
list1.append(16)

# Both list1 and list2 reflect the change, since they reference the same object
print("After appending to list1:")
print("list1:", list1)
print("list2:", list2)