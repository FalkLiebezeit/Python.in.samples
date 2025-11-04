# Efficient exponentiation using a loop (x^n)
# Optimized and commented for clarity

x = 12      # Base value
n = 5       # Exponent
exp = 1     # Initialize result

# Multiply exp by x, n times (iterative exponentiation)
for _ in range(n):
    exp *= x

# Output the result
print(f"{x} to the power of {n} = {exp}")