"""The Collatz Problem - Find and analyze Collatz sequences."""

def collatz(n):
    """
    Compute the Collatz sequence starting from n.

    Args:
        n (int): Starting number (n >= 1).

    Returns:
        list: List of sequence elements until reaching 1.
    """
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2  # Use integer division for even numbers
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def longest_collatz_sequence(limit):
    """
    Find the longest Collatz sequence for all starting numbers up to 'limit'.

    Args:
        limit (int): Maximum starting number to check.

    Returns:
        tuple: (starting_number, sequence) of the longest sequence found.
    """
    max_length = 0
    longest_seq = []
    starting_number = 1

    for start in range(1, limit + 1):
        seq = collatz(start)
        if len(seq) > max_length:
            max_length = len(seq)
            longest_seq = seq
            starting_number = start

    return starting_number, longest_seq

if __name__ == "__main__":
    # --- Set the maximum starting number to check ---
    max_start = 100_000

    # --- Find the longest Collatz sequence up to max_start ---
    start_num, sequence = longest_collatz_sequence(max_start)

    # --- Output the results ---
    print(f"The longest Collatz sequence up to {max_start} starts with {start_num} "
          f"and has {len(sequence)} steps to reach 1.")

    # Optional: Uncomment to print the sequence itself
    # print("Sequence:", sequence)