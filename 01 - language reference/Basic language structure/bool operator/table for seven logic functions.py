# L_10_07.py
# Generate a truth table for seven logic functions (a-g) based on four input bits (D, C, B, A)

print("Nr.\tD\tC\tB\tA\ta\tb\tc\td\te\tf\tg")
decimal = -1  # Counter for the decimal value of the input combination

for D in (0, 1):
    for C in (0, 1):
        for B in (0, 1):
            for A in (0, 1):
                decimal += 1

                # --- Calculate logic functions for each segment ---
                a = D | (A & C) | (B & ~C) | (~A & ~C)
                b = D | ~C | (A & B) | (~A & ~B)
                c = A | C | D | ~B
                d = D | (B & ~A) | (B & ~C) | (~A & ~C) | (A & C & ~B)
                e = ~A & (B | ~C) & (~B | ~D)
                f = D | (C & ~A) | (C & ~B) | (~A & ~B)
                g = D | (B & ~A) | (B & ~C) | (C & ~B)

                # --- Print the results for this input combination ---
                print(decimal, D, C, B, A, int(bool(a)), int(bool(b)), int(bool(c)),
                      int(bool(d)), int(bool(e)), int(bool(f)), int(bool(g)), sep="\t")

# Comments:
# - This script prints a truth table for all 16 combinations of 4 input bits.
# - Each function (a-g) is calculated using bitwise and logical operations.
# - The results are converted to 0/1 using int(bool(...)) for clarity.
# - The table header and output are tab-separated for easy reading.