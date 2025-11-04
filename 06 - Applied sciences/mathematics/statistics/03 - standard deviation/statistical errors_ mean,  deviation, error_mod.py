"""Calculation of statistical errors: mean, standard deviation, and standard error.

This program calculates the mean, standard deviation, and standard error
of a set of measured values using explicit for-loops (not built-in functions).
The output is formatted to show more decimal places.
"""

import math
import numpy as np

# Measured oscillation periods [s]
measurements = np.array([2.05, 1.99, 2.06, 1.97, 2.01,
                         2.00, 2.03, 1.97, 2.02, 1.96])

# Number of measurements
n = measurements.size

# Calculate the mean value
mean = 0
for x in measurements:
    mean += x
mean /= n

# Calculate the standard deviation (sample standard deviation)
std_dev = 0
for x in measurements:
    std_dev += (x - mean) ** 2
std_dev = math.sqrt(std_dev / (n - 1))

# Calculate the standard error of the mean
std_error = std_dev / math.sqrt(n)

# Print results with six decimal places
print(f'Mean:                <T> = {mean:.6f} s')
print(f'Standard deviation: sigma = {std_dev:.6f} s')
print(f'Standard error:  Delta T = {std_error:.6f} s')