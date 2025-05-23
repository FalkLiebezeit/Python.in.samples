
"""
KI:
Write a Python program. 
It should display the active directory and all subdirectories on that level.

answer:
Here's a Python program that will display the active directory and all its subdirectories:

"""

import os

# Get the active (current) directory
current_directory = os.getcwd()

# List all items in the current directory and filter only directories
subdirectories = [d for d in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory, d))]

# Display results
print(f"\nActive Directory:\n {current_directory}\n")
print("Subdirectories at this level:\n")
for subdir in subdirectories:
    print(f"- {subdir}")