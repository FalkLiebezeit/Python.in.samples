import numpy as np

# Set the number of rows and columns for the table
rows = 5
cols = 10
n = rows * cols

# Set the mean (target value) and standard deviation for the normal distribution
mean = 10
std_dev = 1

# Generate n normally distributed random values
values = np.random.normal(mean, std_dev, size=n)

# Round the values to 2 decimal places
rounded_values = np.round(values, decimals=2)

# Sort the rounded values in ascending order
sorted_values = np.sort(rounded_values)

# Reshape the sorted values into a table (column-major order)
table = np.reshape(sorted_values, (rows, cols), order='F')

# Output the results with clear labels
print("Sorted measurement values:\n", sorted_values)
print("Table (column-major order):\n", table)
print("Minimum value:", np.min(rounded_values))
print("Maximum value:", np.max(rounded_values))