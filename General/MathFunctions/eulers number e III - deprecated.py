"""
Copilot:
Create a Python program that calculates Euler's number e.

answer:
Here’s another way to approximate Euler’s number ( e ), using numerical integration. We can approximate ( e ) based on the fact that:
[ \int_1^e \frac{1}{x} ,dx = 1 ]
By solving this numerically, we can estimate ( e ) using an iterative method:
"""
import numpy as np

def calculate_e(steps=1000000):
    """Estimate Euler's number using numerical integration."""
    x_values = np.linspace(1, 3, steps)
    y_values = 1 / x_values
    integral = np.trapz(y_values, x_values)
    
    return 1 + (2 / integral)

# Example usage
print("Approximation of e:", calculate_e())