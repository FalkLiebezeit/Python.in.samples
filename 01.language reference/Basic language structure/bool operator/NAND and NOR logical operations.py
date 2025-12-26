# 03_negation.py
# Demonstrate the NAND and NOR logical operations for all combinations of two boolean variables

print("x1\tx2\tNAND\tNOR")
for x1 in (False, True):
    for x2 in (False, True):
        y1 = not (x1 and x2)   # NAND: Not AND
        y2 = not (x1 or x2)    # NOR: Not OR
        print(x1, x2, y1, y2, sep='\t')

# Comments:
# - The code prints a truth table for the NAND and NOR logical operators.
# - Used 'and' and 'or' for logical operations (preferred over '&' and '|').
# - Used tuple (False, True) for clarity and Pythonic style.