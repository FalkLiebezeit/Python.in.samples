# 02_oder.py
# Demonstrate the logical OR operator (or) with all combinations of two boolean variables

print("x1\tx2\tOR")
for x1 in (False, True):
    for x2 in (False, True):
        y = x1 or x2  # Logical OR operation
        # y = x1 | x2  # Bitwise OR (also works for booleans, but 'or' is preferred for logic)
        print(x1, x2, y, sep='\t')

# Comments:
# - The code prints a truth table for the logical OR operator.
# - 'or' is the logical operator; '|' is the bitwise operator (works similarly for booleans).
# - Used tuple (False, True) for clarity and Pythonic style.