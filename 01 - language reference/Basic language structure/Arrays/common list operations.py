"""Demonstration of common list operations in Python."""

# Create a list with initial values
list1 = [111, 13, 123, 89, 71, 11, 89, 13]

print("Original list:", list1)

# Remove the first occurrence of 13
list1.remove(13)
print("After removing first 13:", list1)

# Remove the element at index 4
list1.pop(4)
print("After removing element at index 4:", list1)

# Insert 33 at index 2
list1.insert(2, 33)
print("After inserting 33 at index 2:", list1)

# Count the number of times 89 appears in the list
print("Count of 89:", list1.count(89))

# Create a second list and extend list1 with it
list2 = [10, 20, 30]
list1.extend(list2)
print("After extending with list2:", list1)

# Reverse the list
list1.reverse()
print("After reversing:", list1)

# Find the index of 111 in the list
print("Index of 111:", list1.index(111))