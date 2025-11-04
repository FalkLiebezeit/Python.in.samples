import re

# Define the string to search in
str1 = "The destination is A!"

# Search for the pattern "destination is" followed by any characters and one of A, B, C, or D
pattern = r"destination is .*(A|B|C|D)"

# Perform the search
result = re.search(pattern, str1)

# Print the matched group if found, otherwise print an error message
if result:
    print("Match found:", result.group())
else:
    print("Unable to search")