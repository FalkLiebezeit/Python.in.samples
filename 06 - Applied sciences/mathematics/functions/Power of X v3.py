def calc_pow(x, n):
    """
    Exponential value calculation using Divide and Conquer technique.
    Efficiently computes x^n using recursion.

    :param x: Base number
    :param n: Exponent
    :return: x raised to the power n
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        half_pow = calc_pow(x, n // 2)  # Compute once and reuse
        return half_pow * half_pow
    else:
        return x * calc_pow(x, n - 1)

# Example usage
x, n = 12, 5
exp_val = calc_pow(x, n)
print(f"{x} to the power of {n} = {exp_val}")