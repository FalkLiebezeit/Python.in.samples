# Demonstrate the logical AND operator (and) with all combinations of two boolean variables

print("x1\tx2\ty")
for x1 in (False, True):
    for x2 in (False, True):
        y = x1 and x2  # Logical AND operation
        # y = x1 & x2  # Bitwise AND (also works for booleans, but 'and' is preferred for logic)
        print(x1, x2, y, sep='\t')

# Comments:
# - The code prints a truth table for the logical AND operator.
# - 'and' is the logical operator; '&' is the bitwise operator (works similarly for booleans).
# - Used tuple (False, True) for clarity and Pythonic style.