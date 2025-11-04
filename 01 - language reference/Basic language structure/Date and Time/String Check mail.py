import re

def check_email(email):
    """
    Check if the provided email address is valid using a regular expression.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Prompt user for an email address
email_input = input("Input an email address: ")

# Validate the email and print the result
if check_email(email_input):
    print(f"{email_input} is Valid")
else:
    print(f"{email_input} is Invalid")