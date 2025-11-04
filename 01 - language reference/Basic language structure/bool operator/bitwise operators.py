# Demonstrate bitwise operators (|, &, ~) with binary output and comments

# --- Bitwise OR (|) ---
print("2 | 2 =", bin(2), "or", bin(2), "=", 2 | 2)
print("3 | 4 =", bin(3), "or", bin(4), "=", 3 | 4)

# --- Bitwise AND (&) ---
print("3 & 8 =", bin(3), "and", bin(8), "=", 3 & 8)
print("2 & 2 =", bin(2), "and", bin(2), "=", 2 & 2)

# --- Bitwise NOT (~) ---
print("~3 =", bin(3), "not", bin(~3), "=", ~3)

# Comments:
# - bin(x) shows the binary representation of x.
# - | is the bitwise OR operator.
# - & is the bitwise AND operator.
# - ~ is the bitwise NOT (inverts all bits, returns -(x+1)).