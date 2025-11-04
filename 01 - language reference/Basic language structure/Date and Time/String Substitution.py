import re

# Define the input string
str1 = "yes I said yes I will Yes."

# Substitute all occurrences of "yes" or "Yes" with "no"
# The pattern "[yY]es" matches both "yes" and "Yes"
res = re.sub(r"[yY]es", "no", str1)

# Print the result after substitution
print(res)