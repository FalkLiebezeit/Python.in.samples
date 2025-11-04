"""Program E13x1.py: Demonstration of defining and calling a function in Python."""

def sum_numbers(num1, num2):
    """
    Return the sum of two numbers.

    Args:
        num1 (int or float): First number.
        num2 (int or float): Second number.

    Returns:
        int or float: The sum of num1 and num2.
    """
    return num1 + num2

def main():
    """Prompt user for two integers and print their sum."""
    try:
        a = int(input('Enter an integer: '))
        b = int(input('Enter another integer: '))
        print('Sum of the numbers =', sum_numbers(a, b))
        print(__name__)
    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()