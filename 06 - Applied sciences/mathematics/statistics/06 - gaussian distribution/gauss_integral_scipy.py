"""Numerical integration of the Gaussian distribution using SciPy.

This script numerically integrates the normalized Gaussian distribution
over a specified interval using scipy.integrate.quad.
"""

import math
import numpy as np
import scipy.integrate

# Standard deviation (sigma) of the Gaussian
sigma = 0.5
# Integration limits: from -x_max to +x_max
x_max = 3

def gauss(x, sigma, x0=0):
    """Compute the normalized Gaussian distribution.

    Args:
        x (float): Value at which to evaluate the function.
        sigma (float): Standard deviation.
        x0 (float, optional): Mean value (default is 0).

    Returns:
        float: Value of the normalized Gaussian at x.
    """
    a = 1 / (math.sqrt(2 * math.pi) * sigma)
    return a * np.exp(- (x - x0) ** 2 / (2 * sigma ** 2))

# Perform the numerical integration of the Gaussian over the interval [-x_max, x_max]
integral, error = scipy.integrate.quad(gauss, -x_max, x_max, args=(sigma,))

# Print the result and the estimated error
print(f'Result of integration: {integral}')
print(f'Estimated error:       {error}')