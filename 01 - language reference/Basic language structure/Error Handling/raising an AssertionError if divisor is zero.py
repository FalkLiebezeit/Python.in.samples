def func_divide(var3, var4):
    """
    Divide var3 by var4, raising an AssertionError if var4 is zero.

    Args:
        var3 (int or float): Numerator.
        var4 (int or float): Denominator.

    Returns:
        float: Result of division.
    """
    assert var4 != 0, "Exception: Division by zero"
    return var3 / var4

# Prompt user for input values and handle invalid input
try:
    var1 = int(input("Enter First Value: "))
    var2 = int(input("Enter Second Value: "))
    output = func_divide(var1, var2)
    print("Result:", output)
except AssertionError as e:
    print(e)
except ValueError:
    print("Error: Please enter valid integer values.")