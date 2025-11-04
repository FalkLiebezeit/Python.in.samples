"""Find the smallest window in a string containing all characters of a pattern.

This script defines a function to find the minimum-length substring in `mainstr`
that contains all characters of `pattern`. If no such window exists, it returns "-1".
"""

total_chars = 256  # Total possible ASCII characters

def smallestWindow(mainstr, pattern):
    """
    Find the smallest window in `mainstr` containing all characters of `pattern`.

    Args:
        mainstr (str): The main string to search in.
        pattern (str): The pattern string whose characters must be present.

    Returns:
        str: The smallest window substring, or "-1" if not possible.
    """
    n = len(mainstr)
    if n < len(pattern):
        return "-1"

    mp = [0] * total_chars  # Frequency map for pattern characters
    start = 0               # Starting index of the answer window
    ans = n + 1             # Length of the answer window (initialized to max)
    cnt = 0                 # Number of unique pattern characters to match

    # Build the frequency map for the pattern
    for ch in pattern:
        mp[ord(ch)] += 1
        if mp[ord(ch)] == 1:
            cnt += 1

    i, j = 0, 0  # Window pointers

    # Traverse the main string with a sliding window
    while j < n:
        mp[ord(mainstr[j])] -= 1
        if mp[ord(mainstr[j])] == 0:
            cnt -= 1

        # When all pattern characters are matched, try to shrink the window
        while cnt == 0:
            if ans > j - i + 1:
                ans = j - i + 1
                start = i

            # Remove the leftmost character and update the map/counter
            mp[ord(mainstr[i])] += 1
            if mp[ord(mainstr[i])] > 0:
                cnt += 1
            i += 1
        j += 1

    if ans > n:
        return "-1"
    return mainstr[start:start + ans]

# --- Driver code ---
if __name__ == "__main__":
    s = 'i am on a seafood diet. i see food and i eat it.'
    t = 'fast'
    small_window = smallestWindow(s, t)
    if small_window == "-1":
        print("No such window possible")
    else:
        print(f'Window is "{small_window}" and minimum length of the substring is {len(small_window)}')