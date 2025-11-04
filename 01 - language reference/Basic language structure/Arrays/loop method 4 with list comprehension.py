# Loop through a list using list comprehension (method 4)

flowers = ['lily', 'rose', 'jasmine', 'sunflower']  # List of flower names

# --- Print each flower using a list comprehension ---
[print(flower) for flower in flowers]

# Note:
# Using a list comprehension for side effects (like print) is not recommended.
# A simple for loop is more Pythonic for this purpose.