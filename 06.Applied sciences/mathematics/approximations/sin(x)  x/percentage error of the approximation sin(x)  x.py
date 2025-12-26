"""Calculation of the percentage error of the approximation sin(x) ≈ x.

This script computes the percentage error of the approximation
sin(x) ≈ x for angles from 5 degrees to 90 degrees in 5-degree steps.
The results are stored in NumPy arrays and printed.
"""

import numpy as np

# Create an array of angles in degrees from 5 to 90 (inclusive) in 5-degree steps
angles_deg = np.arange(5, 95, 5)

# Convert the angles to radians
x = np.radians(angles_deg)

# Calculate the percentage error of the approximation sin(x) ≈ x
# Error formula: 100 * (approximation - exact) / exact
percent_error = 100 * (x - np.sin(x)) / np.sin(x)

# Print the results
print("Angle [deg]:", angles_deg)
print("Percent error [%]:", percent_error)