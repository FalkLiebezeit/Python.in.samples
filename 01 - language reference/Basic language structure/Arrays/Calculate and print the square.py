"""Calculate and print the square of a user-provided number."""

def square(num):
    """Return the square of the given number."""
    return num ** 2

# Prompt the user for input and convert to integer
n = int(input('Enter a number: '))

# Output the result with a clear message
print('The square of the number is:', square(n))