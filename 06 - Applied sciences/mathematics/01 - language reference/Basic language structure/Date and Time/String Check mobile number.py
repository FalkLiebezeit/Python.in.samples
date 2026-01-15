import re

def mobile_validate(mobileno):
    """
    Validate a mobile number using a regular expression.

    Args:
        mobileno (str): The mobile number to validate.

    Returns:
        bool: True if valid (exactly 10 digits), False otherwise.
    """
    # Regular expression pattern for a 10-digit mobile number
    pattern = r'^\d{10}$'
    return bool(re.match(pattern, mobileno))

# Prompt user for mobile number input
mobileno = input("Enter Your Mobile Number: ")

# Validate the mobile number and print the result
if mobile_validate(mobileno):
    print(f"{mobileno} is a valid Mobile number.")
else:
    print(f"{mobileno} is not a valid Mobile number.")