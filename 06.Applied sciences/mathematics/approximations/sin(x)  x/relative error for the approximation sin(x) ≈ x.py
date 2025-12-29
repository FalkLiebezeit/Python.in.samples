"""Calculation of the relative error for the approximation sin(x) ≈ x.

This script computes the relative error (in percent) of the approximation
sin(x) ≈ x for angles from 5° to 90° in 5-degree steps.
The results are stored in two lists and printed.
"""

import math

# Create a list of angles in degrees (5° to 90° in 5-degree steps)
angle_list = list(range(5, 95, 5))

# Initialize an empty list for the relative errors in percent
relative_error_list = []

# Compute the relative error for each angle
for angle_deg in angle_list:
    x_rad = math.radians(angle_deg)  # Convert angle to radians
    # Calculate the relative error in percent
    rel_error = 100 * (x_rad - math.sin(x_rad)) / math.sin(x_rad)
    relative_error_list.append(rel_error)

# Output the results with clear labels
print("Angles (degrees):")
print(angle_list)
print("Relative errors (%):")
print(relative_error_list)