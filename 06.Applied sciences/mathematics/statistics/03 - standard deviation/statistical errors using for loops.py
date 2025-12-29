"""Calculation of statistical errors: mean, standard deviation, and standard error.

This script calculates the mean, sample standard deviation, and standard error
of a set of measured values using explicit for-loops (without built-in functions).
The output is formatted to show two decimal places.
"""

import math
import numpy as np

# Measured oscillation periods [s]
measurements = np.array([2.05, 1.99, 2.06, 1.97, 2.01,
                         2.00, 2.03, 1.97, 2.02, 1.96])


# Number of measurements
n = measurements.size

# Calculate the mean value using a for-loop
mean = 0
for x in measurements:
    mean += x
mean /= n

# Calculate the sample standard deviation using a for-loop
std_dev = 0
for x in measurements:
    std_dev += (x - mean) ** 2
std_dev = math.sqrt(std_dev / (n - 1))

# Calculate the standard error of the mean
std_error = std_dev / math.sqrt(n)

# Print results with two decimal places
print(f'Mean:                <T> = {mean:.2f} s')
print(f'Standard deviation: sigma = {std_dev:.2f} s')
print(f'Standard error:  Delta T = {std_error:.2f} s')