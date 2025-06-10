"""
Copilot:
Create a Python program that calculates Euler's number e.

answer:
This program calculates ( e ) using the series:
[ e = \sum_{n=0}^{\infty} \frac{1}{n!} ]
By adjusting the precision parameter, you can control how many terms of the series are used, improving the accuracy.
"""

import math

def calculate_e(precision=20):
    """Calculate Euler's number using the series expansion."""
    e = sum(1 / math.factorial(n) for n in range(precision))
    return e

# Example usage
print("Approximation of e:", calculate_e(20))