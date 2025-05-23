
"""
KI:
Write a Python program. 
It should display the active directory and all subdirectories on that level starting with the letter 'T'.

answer:
Here's a Python program that will display the active directory and all its subdirectories:

"""

import os

# Get the current working directory
current_directory = os.getcwd()

# List all subdirectories that start with 'T'
subdirectories = [d for d in os.listdir(current_directory) 
                  if os.path.isdir(os.path.join(current_directory, d)) and d.startswith('T')]

# Display results
print(f"\n\nActive Directory: {current_directory}\n")
print("Subdirectories starting with 'T':\n")
      
for subdir in subdirectories:
    print(f"- {subdir}")

print("\n")