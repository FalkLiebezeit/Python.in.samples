def factorial(n):
    """Recursively calculates the factorial of a given number n."""
    print(f"factorial has been called with n = {n}")  # Debugging statement to track recursive calls
    
    if n == 1:
        return 1  # Base case: factorial of 1 is 1
    else:
        res = n * factorial(n - 1)  # Recursive step: multiply n by factorial of (n-1)
        print(f"track {n} * factorial({n-1}): {res}")  # Debugging statement to track calculations
        return res

# Test the function with an example
print(factorial(5))  