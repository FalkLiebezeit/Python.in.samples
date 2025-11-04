import re

# Regular expression for checking if the input contains only integer digits
pattern = r'^[0-9]+$'

# Prompt user for their roll number
rollno = input("Enter Your Rollno: ")

# Validate the input and print the result
if re.fullmatch(pattern, rollno):
    print("Welcome:", rollno)
else:
    print("Wrong Input, enter only integer digits.")