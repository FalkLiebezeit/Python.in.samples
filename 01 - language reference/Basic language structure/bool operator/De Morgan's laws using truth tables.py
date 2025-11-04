"""Demonstration of De Morgan's laws using truth tables."""

# Print the header for the truth table
print("x1\t x2\t y1\t y2\t y3\t y4")
print("  \t   \t¬(x1∧x2)\t¬x1∨¬x2\t¬(x1∨x2)\t¬x1∧¬x2")

# Iterate over all combinations of x1 and x2 (False, True)
for x1 in (False, True):
    for x2 in (False, True):
        # Apply De Morgan's laws
        y1 = not (x1 and x2)         # ¬(x1 ∧ x2)
        y2 = (not x1) or (not x2)    # ¬x1 ∨ ¬x2
        y3 = not (x1 or x2)          # ¬(x1 ∨ x2)
        y4 = (not x1) and (not x2)   # ¬x1 ∧ ¬x2
        # Print the results in tabular format
        print(x1, x2, y1, y2, y3, y4, sep='\t')