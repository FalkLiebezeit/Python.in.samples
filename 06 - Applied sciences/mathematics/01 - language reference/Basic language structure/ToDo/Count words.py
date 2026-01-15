def total(initial=10, *numbers, **keywords):
    """
    Calculate the total sum of an initial value, positional arguments, and keyword arguments.

    Parameters:
    initial (int, optional): The starting value of the sum. Default is 10.
    *numbers (tuple): Additional numbers to be added.
    **keywords (dict): Named arguments representing additional values to be added.

    Returns:
    int: The computed total sum.
    """
    count = initial  # Start with the initial value

    # Sum up all positional arguments
    for num in numbers:
        count += num

    # Sum up all keyword argument values
    for value in keywords.values():
        count += value

    return count  # Return the final computed total

# Example usage
print(total(10, 5, 10, 15, twenty=20, thirty=30, fifty=50))