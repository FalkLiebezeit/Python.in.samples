"""
KI:
Write a Python program. 
It should display the active directory and all subdirectories.

answer:
Here's a Python program that will display the active directory and all its subdirectories:

"""

import os

def list_directories(start_path):
    for root, dirs, files in os.walk(start_path):
        print(root)

# Get the current working directory
current_directory = os.getcwd()

# Display the active directory
print(f"\nActive Directory: {current_directory}\n")

input("\nPress Enter to continue \n")

print(f"\nActive Directory and Subdirectories:\n")
list_directories(current_directory)