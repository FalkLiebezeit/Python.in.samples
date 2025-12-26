# Simplify a complex boolean logic expression using sympy

from sympy.logic import simplify_logic
from sympy import symbols

# --- Define boolean variables ---
D, C, B, A = symbols('D C B A')

# --- Construct the minterms as given ---
c2  = ( D |  C | ~B |  A)
c10 = (~D |  C | ~B |  A)
c11 = (~D |  C | ~B | ~A)
c12 = (~D | ~C |  B |  A)
c13 = (~D | ~C |  B | ~A)
c14 = (~D | ~C | ~B |  A)
c15 = (~D | ~C | ~B | ~A)

# --- Combine all minterms with AND to form the function ---
c = c2 & c10 & c11 & c12 & c13 & c14 & c15

# --- Simplify the boolean expression ---
simplified_c = simplify_logic(c)

# --- Output the simplified expression ---
print("Simplified c =", simplified_c)

'''
Solution from literature (Beuth, Digitaltechnik)
determined using disjunctive normal form (DNF):
c = A | ~B | C
'''