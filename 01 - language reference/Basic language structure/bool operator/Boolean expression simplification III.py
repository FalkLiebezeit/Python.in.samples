"""Boolean expression simplification using sympy.

This script defines several complex boolean expressions with four variables,
combines them using logical AND, and simplifies the result.
"""

from sympy.logic import simplify_logic
from sympy import symbols

# Define boolean variables
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')

# Define the individual boolean expressions
y1 = ( x1 | ~x2 |  x3 | ~x4)  
y2 = ( x1 | ~x2 | ~x3 |  x4)
y3 = ( x1 | ~x2 | ~x3 | ~x4)
y4 = (~x1 |  x2 |  x3 | ~x4)
y5 = (~x1 | ~x2 |  x3 |  x4)
y6 = (~x1 | ~x2 |  x3 | ~x4)

# Combine all expressions using logical AND
y = y1 & y2 & y3 & y4 & y5 & y6

# Simplify the combined boolean expression
simplified_y = simplify_logic(y)

# Output the simplified result
print("Simplified expression y =", simplified_y)