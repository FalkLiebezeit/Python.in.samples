# Age checking program
# If the entered age is greater than 100, do nothing (use pass)
# Otherwise, print a welcome message

age = int(input("Enter your age: "))  # Get user input and convert it to an integer

if age > 100:
    pass  # No action is taken when age is greater than 100
else:
    print("Your age is:", age)  # Print the entered age if it is 100 or less

print('Welcome User!!')  # Always prints the welcome message