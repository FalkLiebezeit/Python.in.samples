# Demonstration of basic list operations in Python
# Lists are mutable sequences that can store multiple values of any type
# Index starts at 0, so a[0] is the first element

# --- Initialize the list ---
numbers = [56, 57, 89]  # More descriptive variable name

# --- Access and print the first element (index 0) ---
first_element = numbers[0]  # Using meaningful variable names
print(f"The first element (index 0) is: {first_element}")  # Using f-string for cleaner formatting

# --- Append a new element to the end of the list ---
numbers.append(90)  # append() method adds element at the end
print(f"List after append: {numbers}")  # Show the current state

# --- Access and print the newly added element (last position) ---
last_element = numbers[-1]  # Using -1 index to get last element
print(f"The last element is: {last_element}")

# --- Find and print the length of the list ---
list_length = len(numbers)  # len() returns the number of elements
print(f'The length of the list is: {list_length}')