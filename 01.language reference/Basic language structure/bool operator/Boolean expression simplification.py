"""Boolean expression simplification using sympy.

This script defines a complex boolean expression with four variables,
combines multiple terms using logical AND and OR, and simplifies the result.
"""

from sympy.logic import simplify_logic
from sympy import symbols

# Define boolean variables
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')

# Define the terms of the boolean expression
terms = [
    (~x1 & ~x2 & ~x3 & ~x4),
    (~x1 & ~x2 & ~x3 &  x4),
    (~x1 & ~x2 &  x3 & ~x4),
    (~x1 & ~x2 &  x3 &  x4),
    (~x1 &  x2 & ~x3 & ~x4),
    ( x1 & ~x2 & ~x3 & ~x4),
    ( x1 & ~x2 &  x3 & ~x4),
    ( x1 & ~x2 &  x3 &  x4),
    ( x1 &  x2 &  x3 & ~x4),
    ( x1 &  x2 &  x3 &  x4)
]

# Combine all terms using logical OR
y = terms[0]
for term in terms[1:]:
    y |= term

# Simplify the boolean expression
simplified_y = simplify_logic(y)

# Output the simplified result
print("Simplified expression y =", simplified_y)