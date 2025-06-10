# Function to reverse a number
def reverse(number):
    """Returns the reversed version of the given number."""
    rev = 0
    while number > 0:
        rev = rev * 10 + (number % 10)  # Extracts and appends the last digit
        number //= 10  # Removes the last digit from the number
    return rev

# Function to multiply a number by 2
def multiply(number):
    """Prints double the given number."""
    print(f'Double of the number: {2 * number}')

# Function to add all digits of a number
def add_digits(number):
    """Returns the sum of all digits in the given number."""
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10  # Extracts and adds the last digit
        number //= 10  # Removes the last digit
    return sum_digits

# Main function to execute user input and process operations
def main():
    try:
        num = int(input('Enter a number: '))  # Ensures input is an integer
        
        if num % 2 == 1:  # If number is odd, reverse it
            print(f'Reverse of the typed number: {reverse(num)}')
        else:  # If number is even, multiply it
            multiply(num)

        if num % 3 == 0:  # If number is divisible by 3, sum its digits
            print(f'Sum of digits: {add_digits(num)}')
    
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()  # Call main function