# 03_schreiben.py
# Generate normally distributed random values, round them, and save to a text file

import numpy as np

# Number of random values to generate
n = 50
# Mean (target value) and standard deviation for the normal distribution
mean = 50
std_dev = 1

# Generate n normally distributed random values
values = np.random.normal(mean, std_dev, size=n)

# Round the values to 2 decimal places for display
rounded_values = np.round(values, decimals=2)

# Save the original values (not rounded) to a text file with 2 decimal places
np.savetxt("daten.txt", values, fmt="%4.2f")

# Output the rounded values and their type
print("Normally distributed values:")
print(rounded_values)
print("Type of values:", type(values))