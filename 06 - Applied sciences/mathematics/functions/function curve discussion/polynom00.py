"""
Ki:

Write a Python program that solves the following task:

- Write a function that calculates and outputs a third-degree polynomial in the form
f(x) = 2 * x^3 + 3 * x^2 + 4 * x + 5
.
- Calculate the zeros of the polynomial and output them.
- Calculate the derivatives of the polynomial and output them.
- Plot the function in the coordinate system

"""

import numpy as np
import matplotlib.pyplot as plt

# --- Define the polynomial and its derivatives ---
def f(x):
    """Compute the polynomial f(x) = 2x^3 + 3x^2 + 4x + 5."""
    return 2 * x**3 + 3 * x**2 + 4 * x + 5

def f_derivative(x):
    """Compute the first derivative: f'(x) = 6x^2 + 6x + 4."""
    return 6 * x**2 + 6 * x + 4

def f_second_derivative(x):
    """Compute the second derivative: f''(x) = 12x + 6."""
    return 12 * x + 6

def f_third_derivative(x):
    """Compute the third derivative: f'''(x) = 12."""
    return 12

# --- Calculate zeros of the polynomial ---
coeffs = [2, 3, 4, 5]  # Coefficients for 2x^3 + 3x^2 + 4x + 5
zeros = np.roots(coeffs)
print("Zeros of the polynomial f(x) = 2x^3 + 3x^2 + 4x + 5:")
for idx, root in enumerate(zeros, 1):
    print(f"Zero {idx}: {root}")

# --- Output the derivatives as formulas ---
print("\nFirst derivative:   f'(x) = 6x^2 + 6x + 4")
print("Second derivative:  f''(x) = 12x + 6")
print("Third derivative:   f'''(x) = 12")

# --- Plot the polynomial function ---
x = np.linspace(-5, 3, 400)  # Range of x values for plotting
y = f(x)

plt.figure(figsize=(8, 6))  # Set figure size for better visibility
plt.plot(x, y, label=r"$f(x) = 2x^3 + 3x^2 + 4x + 5$", color='blue')
plt.axhline(0, color='black', linewidth=0.8)  # Draw x-axis
plt.axvline(0, color='black', linewidth=0.8)  # Draw y-axis
plt.title("Plot of the polynomial $f(x) = 2x^3 + 3x^2 + 4x + 5$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()