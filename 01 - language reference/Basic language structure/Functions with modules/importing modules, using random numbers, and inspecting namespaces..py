# Demonstration of importing modules, using random numbers, and inspecting namespaces.

import sum  # Custom module with an 'add' function
import random

# Generate random integers for demonstration
var1 = random.randint(3, 9)
print('var1 =', var1)
var2 = random.randint(4, 8)
print('var2 =', var2)
var3 = random.randint(12, 34)
print('var3 =', var3)

# Use the add function from the sum module to add three numbers
print("Sum of values:", sum.add(var1, var2, var3))

# Display the current local namespace as a dictionary
print("Local namespace:", vars())

# Display the namespace of the sum module
print("sum module namespace:", vars(sum))

# Display the namespace of the random module
print("random module namespace:", vars(random))