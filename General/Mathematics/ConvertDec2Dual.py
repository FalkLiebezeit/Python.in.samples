"""
Ki:

WWrite a Python program. The user should enter a decimal number. 
The program should convert this number to a binary number.
answer:

Optimizations & Improvements
- Encapsulation: Introduced a separate get_user_input() function for better readability and reusability.
- Loop for Input Validation: Ensures valid integer input without crashing the program.
- Improved Error Handling: Prevents incorrect entries and allows users to retry input.
- Enhanced Documentation: Added detailed docstrings for functions to improve clarity and maintainability.
60
"""


def decimal_to_binary(n):
    """
    Convert a decimal number to its binary representation.
    
    Args:
        n (int): The decimal number to convert.
    
    Returns:
        str: Binary representation of the decimal number.
    """
    return bin(n)[2:]  # Convert using bin() and remove '0b' prefix

def get_user_input():
    """
    Get a valid integer input from the user.
    
    Returns:
        int: Valid decimal number entered by the user.
    """
    while True:
        try:
            num = int(input("Enter a decimal number: "))  # Prompt user input
            if num < 0:
                print("Please enter a non-negative number.")  # Ensure input is non-negative
            else:
                return num  # Return valid input
        except ValueError:
            print("Invalid input! Please enter a valid integer.")  # Handle non-integer inputs

def main():
    """Main function to get input and display the binary representation."""

    num = get_user_input()  # Get valid user input
    binary_representation = decimal_to_binary(num)  # Convert to binary

    print(f"\nBinary representation of {num}: {binary_representation}\n")  # Display result

if __name__ == "__main__":
    main()  # Execute the main function