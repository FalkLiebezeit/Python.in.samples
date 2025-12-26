import numpy as np

# Number of random values to generate
n = 10
# Mean (target value) and standard deviation for the normal distribution
mean = 50
std_dev = 1

# Generate n normally distributed random values
values = np.random.normal(mean, std_dev, size=n)

# Round the values to 2 decimal places
rounded_values = np.round(values, decimals=2)

# Output the results with clear labels
print("Normally distributed values:")
print(values)
print("Rounded values:")
print(rounded_values)
print("Type of values:", type(values))