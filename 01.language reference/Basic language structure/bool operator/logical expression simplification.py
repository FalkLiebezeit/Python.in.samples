# L_10_04.py
# Demonstrate logical expression simplification using sympy

from sympy.logic import simplify_logic
from sympy import symbols

# --- Define boolean variables ---
x1, x2, x3 = symbols('x1 x2 x3')

# --- Construct the logical expression ---
# y = (not x1 and x2 and not x3) or (x1 and not x2 and not x3) or (x1 and x2 and not x3)
y = (~x1 & x2 & ~x3) | (x1 & ~x2 & ~x3) | (x1 & x2 & ~x3)

# --- Simplify the logical expression ---
simplified_y = simplify_logic(y)

# --- Output the simplified expression ---
print("Original expression:")
print(y)
print("\nSimplified expression:")
print(simplified_y)

# Comments:
# - This script uses sympy to simplify a boolean logic expression.
# - The original and simplified expressions are printed for comparison.
# - '~' is logical NOT, '&' is AND, '|' is OR in sympy.