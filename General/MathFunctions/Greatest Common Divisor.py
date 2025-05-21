# Finding the Greatest Common Divisor (GCD) of two numbers using recursion

def gcd(num1, num2):  # Function definition
    if num2 == 0:  # Base case: If num2 is zero, return num1
        return num1
    else:  # Recursive calculation of the GCD
        return gcd(num2, num1 % num2)

# Main function for user input and computation
def main():
    try:
        # Using int(input()) instead of eval(input()), since eval can be unsafe
        a = int(input('Enter an integer: '))
        b = int(input('Enter an integer: '))

        # Ensure 'a' is the larger number without using a temporary variable
        if b > a:    
            a, b = b, a  # Pythonic way to swap values

        result = gcd(a, b)  # Compute GCD
        print('GCD of', a, 'and', b, '= ', result)

    except ValueError:  # Error handling for invalid input
        print("Invalid input! Please enter valid integers.")

main()  # Call the main function