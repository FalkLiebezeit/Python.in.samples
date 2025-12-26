"""
pip install sympy

"""
from sympy import symbols, diff, integrate

# Define the symbolic variable
x = symbols("x")

# Define the polynomial function
y = x**3 - 7*x**2 + 7*x + 15

# Compute the first, second, and third derivatives
y_1 = diff(y, x, 1)  # First derivative
y_2 = diff(y, x, 2)  # Second derivative
y_3 = diff(y, x, 3)  # Third derivative

# Compute the indefinite integral
Y = integrate(y, x)

# Print the results
print("1st derivative:   ", y_1)
print("2nd derivative:   ", y_2)
print("3rd derivative:   ", y_3)
print("Indefinite integral:", Y)