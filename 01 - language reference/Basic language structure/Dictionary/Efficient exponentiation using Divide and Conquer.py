def calc_pow(x, n):
    """
    Efficient exponentiation using Divide and Conquer (Exponentiation by Squaring).

    Args:
        x (float or int): Base number.
        n (int): Exponent (should be non-negative).

    Returns:
        float or int: x raised to the power n.
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        half = calc_pow(x, n // 2)
        return half * half
    else:
        return x * calc_pow(x, n - 1)

# Example usage
x, n = 12, 5
exp_val = calc_pow(x, n)
print(f"{x} to the power of {n} = {exp_val}")