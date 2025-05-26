# Function to calculate exponentiation of a number recursively
def expo(base, exp):
    """Recursively computes base^exp."""
    if exp == 0:  # Base case: any number to the power of 0 is 1
        return 1
    elif exp == 1:  # Base case: any number to the power of 1 is itself
        return base
    else:  # Recursive case: multiply base by the recursive call with decremented exponent
        return base * expo(base, exp - 1)

# Main function to execute user input and print results
def main():
    try:
        x = float(input("Enter base: "))  # Accept float values for broader input cases
        y = int(input("Enter integer for exponential value: "))  # Ensure exponent is an integer
        
        if y < 0:  # Handle negative exponents
            print(f"Exponent should be non-negative, but computing its reciprocal: {expo(x, -y)}")
            print(f"Result: {1 / expo(x, -y)}")
        else:
            print(f"Result: {expo(x, y)}")
    except ValueError:
        print("Invalid input! Base should be a number and exponent an integer.")

main()
