"""
Ki:

Write a Python program. The user should enter a number. 
The program should display all Fibonacci numbers smaller than this number.

answer:

Optimizations:
- Encapsulation: Separated logic into functions (generate_fibonacci and main) for better readability and maintainability.
- Improved Loop Condition: Using while True with a break statement simplifies the loop.
- Error Handling: Added exception handling to manage invalid inputs gracefully.
- Input Validation: Ensures that only positive numbers are accepted.


"""

def generate_fibonacci(limit):
    """Generate a list of Fibonacci numbers smaller than the given limit."""
    fib_sequence = [0, 1]  # Initialize the sequence with the first two numbers
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]  # Calculate the next Fibonacci number
        if next_fib >= limit:
            break  # Stop if the next number exceeds the limit
        fib_sequence.append(next_fib)  # Append the number to the sequence
    return fib_sequence

def main():
    """Main function to get user input and display Fibonacci numbers."""
    try:
        num = int(input("Enter a number: "))  # Get input from the user
        if num < 0:
            print("Please enter a positive number.")
        else:
            fib_list = generate_fibonacci(num)  # Generate Fibonacci numbers
            print(f"\nFibonacci numbers smaller than {num}: {fib_list}\n600")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")  # Handle non-integer inputs

if __name__ == "__main__":
    main()  # Execute the main function