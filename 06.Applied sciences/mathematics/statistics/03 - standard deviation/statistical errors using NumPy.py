"""Calculation of statistical errors using NumPy.

This program calculates the mean, standard deviation (sample), and standard error
of a set of measured values using NumPy's built-in functions.

The output is formatted to show six decimal places.
The argument ddof=1 ensures the correct calculation of the sample standard deviation.
"""

import math
import numpy as np

# Measured oscillation periods [s]
measurements = np.array([2.05, 1.99, 2.06, 1.97, 2.01,
                         2.00, 2.03, 1.97, 2.02, 1.96])

# Calculate mean value
mean = np.mean(measurements)

# Calculate sample standard deviation (ddof=1 for unbiased estimator)
std_dev = np.std(measurements, ddof=1)

# Calculate standard error of the mean
std_error = std_dev / math.sqrt(measurements.size)

# Print results with six decimal places
print(f'Mean:                <T> = {mean:.6f} s')
print(f'Standard deviation: sigma = {std_dev:.6f} s')
print(f'Standard error:  Delta T = {std_error:.6f} s')