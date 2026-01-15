# Demonstrate the XOR (exclusive OR) logical operation for all combinations of two boolean variables

print("x1\tx2\tXOR")
for x1 in (False, True):
    for x2 in (False, True):
        # XOR: True if exactly one of x1 or x2 is True
        y = (x1 and not x2) or (not x1 and x2)
        print(x1, x2, y, sep="\t")

# Comments:
# - The code prints a truth table for the logical XOR operation.
# - XOR is True if exactly one input is True, otherwise False.
# - Used tuple (False, True) for clarity and Pythonic style.