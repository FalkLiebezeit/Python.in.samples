"""Boolean logic simplification for seven-segment display control.

This script defines the logic expressions for segments a-g of a seven-segment display
using four input variables (D, C, B, A), simplifies each expression, and prints the result.
"""

from sympy.logic import simplify_logic
from sympy import symbols

# Define input variables for the seven-segment decoder
D, C, B, A = symbols('D C B A')

# Define the logic expressions for each segment
a = (D | C | B | ~A) & (D | ~C | B | A) & (D | ~C | ~B | A)
b = (D | ~C | B | ~A) & (D | ~C | ~B | A)
c = (D | C | ~B | A)
d = (D | C | B | ~A) & (D | ~C | B | A) & (D | ~C | ~B | ~A)
e = (~D & ~C & ~B & ~A) | (~D & ~C & B & ~A) | (~D & C & B & ~A) | (D & ~C & ~B & ~A)
f = (D | C | B | ~A) & (D | C | ~B | A) & (D | C | ~B | ~A) & (D | ~C | ~B | ~A)
g = (D | C | B | A) & (D | C | B | ~A) & (D | ~C | ~B | ~A)

# Simplify and print each segment's logic expression
print("Simplified logic for seven-segment display:")
print("a =", simplify_logic(a))
print("b =", simplify_logic(b))
print("c =", simplify_logic(c))
print("d =", simplify_logic(d))
print("e =", simplify_logic(e))
print("f =", simplify_logic(f))
print("g =", simplify_logic(g))