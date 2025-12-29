# L_10_05.py
# Demonstrate simplification of a boolean logic expression using sympy

from sympy.logic import simplify_logic
from sympy import symbols

# --- Define boolean variables ---
m1, m2, m3 = symbols('m1 m2 m3')

# --- Construct the logical expression ---
# y = (m1 AND NOT m2 AND m3) OR (NOT m1 AND m2 AND m3) OR (m1 AND m2 AND m3)
y = (m1 & ~m2 & m3) | (~m1 & m2 & m3) | (m1 & m2 & m3)

# --- Simplify the logical expression ---
simplified_y = simplify_logic(y)

# --- Output the simplified expression ---
print("Original expression:")
print(y)
print("\nSimplified expression:")
print(simplified_y)

# Comments:
# - This script uses sympy to simplify a boolean logic expression.
# - '~' is logical NOT, '&' is AND, '|' is OR in sympy.
# - Both the original and simplified expressions are printed for comparison.