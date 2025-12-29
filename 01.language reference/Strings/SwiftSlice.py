# Total possible characters in ASCII
TOTAL_CHARS = 256

def smallest_window(main_str, pattern):
    """Finds the smallest substring in main_str that contains all characters of pattern."""
    n = len(main_str)
    if n < len(pattern):
        return "-1"
    
    # Character frequency map for pattern
    char_count = [0] * TOTAL_CHARS
    required_chars = 0

    # Populate character frequency for pattern
    for char in pattern:
        char_count[ord(char)] += 1
        if char_count[ord(char)] == 1:
            required_chars += 1

    # Sliding window pointers
    start_idx, min_length = 0, float('inf')
    left, right = 0, 0
    matched_chars = required_chars

    # Traverse through main_str
    while right < n:
        # Reduce count of the current character in map
        char_count[ord(main_str[right])] -= 1
        if char_count[ord(main_str[right])] == 0:
            matched_chars -= 1

        # Try to shrink the window when all characters are matched
        while matched_chars == 0:
            if min_length > right - left + 1:
                min_length = right - left + 1
                start_idx = left

            # Restore count for left-most character and move left pointer
            char_count[ord(main_str[left])] += 1
            if char_count[ord(main_str[left])] > 0:
                matched_chars += 1
            left += 1
        
        right += 1

    # If no valid window found, return "-1"
    return "-1" if min_length == float('inf') else main_str[start_idx:start_idx + min_length]

# Driver code
s = "i am on a seafood diet. i see food and i eat it."
t = "fast"

small_window = smallest_window(s, t)

if small_window == "-1":
    print("No such window possible")
else:
    print(f'Window is "{small_window}" with minimum length {len(small_window)}')