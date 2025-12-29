"""Calculation of the relative error for the approximation sin(x) ≈ x.

This script computes and prints the relative error (in percent) of the approximation
sin(x) ≈ x for angles from 5° to 90° in 5-degree steps.
"""

import math

# Loop over angles from 5° to 90° in 5-degree steps
for angle_deg in range(5, 95, 5):
    x_rad = math.radians(angle_deg)  # Convert angle to radians
    # Calculate the relative error in percent
    # Error formula: (approximation - true value) / true value * 100%
    rel_error = 100 * (x_rad - math.sin(x_rad)) / math.sin(x_rad)
    # Print the result with formatted output
    print(f'Angle: {angle_deg:2} deg, Relative error: {rel_error:5.1f} %')