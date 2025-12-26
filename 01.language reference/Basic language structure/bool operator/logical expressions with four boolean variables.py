# L_10_03.py
# Demonstrate logical expressions with four boolean variables and compare two forms

print("x1\tx2\tx3\tx4\ty1\ty2")
for x1 in (False, True):
    for x2 in (False, True):
        for x3 in (False, True):
            for x4 in (False, True):
                # y1: (not x1 or x2 or x3) and not (x1 or x4)
                y1 = (not x1 or x2 or x3) and not (x1 or x4)
                # y2: not x1 and not x4 (simplified form)
                y2 = not x1 and not x4
                print(x1, x2, x3, x4, y1, y2, sep="\t")

# Comments:
# - The code prints a truth table for two logical expressions (y1 and y2) with four variables.
# - y1 is a compound logical expression; y2 is its simplified form.
# - Used tuple (False, True) for clarity and Pythonic style.
# - Tab-separated output for easy reading.