"""
Copilot:
Create a Python program that calculates Euler's number e.

answer:
Here is an alternative method to calculate Euler’s number ( e ), using the limit definition:
[ e = \lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n ]
The Python program uses a large number for ( n ) to approximate ( e ):


"""

def calculate_e(limit=1000000):
    """Calculate Euler's number using the limit definition."""
    return (1 + 1 / limit) ** limit

# Example usage
print("Approximation of e:", calculate_e())