# 05_distributiv.py
# Demonstrate distributive laws for logical AND and OR with all combinations of three boolean variables

print("x1\tx2\tx3\ty1\t\ty2\t\ty3\t\ty4")
print("-------------------------------------------------------------")
for x1 in (False, True):
    for x2 in (False, True):
        for x3 in (False, True):
            y1 = (x1 and x2) or (x1 and x3)      # Distributive: x1 and (x2 or x3) == (x1 and x2) or (x1 and x3)
            y2 = x1 and (x2 or x3)
            y3 = (x1 or x2) and (x1 or x3)       # Distributive: x1 or (x2 and x3) == (x1 or x2) and (x1 or x3)
            y4 = x1 or (x2 and x3)
            print(f"{x1}\t{x2}\t{x3}\t{y1}\t{y2}\t{y3}\t{y4}")

# Comments:
# - y1 and y2 demonstrate the distributive law: x1 and (x2 or x3) == (x1 and x2) or (x1 and x3)
# - y3 and y4 demonstrate the distributive law: x1 or (x2 and x3) == (x1 or x2) and (x1 or x3)
# - The code prints a truth table for all combinations of x1, x2, x3.
# - Used tuple (False, True) for clarity and Pythonic style.