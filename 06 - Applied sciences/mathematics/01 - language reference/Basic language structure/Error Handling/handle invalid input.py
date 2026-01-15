import sys

# Prompt the user to enter a number and handle invalid input
try:
    no = int(input("Enter a number: "))
except ValueError:
    print("Error: Please enter only numbers.")
    sys.exit()

# Print the entered number if input is valid
print("You entered number:", no)