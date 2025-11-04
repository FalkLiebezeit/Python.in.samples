"""Curve fitting: Drag force as a function of velocity.

This script fits a power-law model to measured drag force data as a function of velocity,
estimates the fit parameters and their uncertainties, and visualizes the results with error bars.
"""

import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

# Measured velocities [m/s]
measured_v = np.array([5.8, 7.3, 8.9, 10.6, 11.2])

# Uncertainties in velocity [m/s]
error_v = np.array([0.3, 0.3, 0.2, 0.2, 0.1])

# Measured forces [N]
measured_F = np.array([0.10, 0.15, 0.22, 0.33, 0.36])

# Uncertainties in force [N]
error_F = np.array([0.02, 0.02, 0.02, 0.02, 0.02])

def fit_function(v, b, n):
    """Model function: Drag force as a power law of velocity."""
    return b * v ** n

# Perform the curve fitting using non-linear least squares
# Initial guesses: b=1.5, n=2.0; use force uncertainties as weights
popt, pcov = scipy.optimize.curve_fit(
    fit_function, measured_v, measured_F, p0=[1.5, 2.0], sigma=error_F, absolute_sigma=True
)
fit_b, fit_n = popt
error_b, error_n = np.sqrt(np.diag(pcov))

# Print the results of the curve fitting
print('Curve fitting results:')
print(f'  b = ({fit_b:.4f} ± {error_b:.4f}) N / (m/s)^n')
print(f'  n = {fit_n:.2f} ± {error_n:.2f}')

# Create the figure and axes
fig, ax = plt.subplots()
ax.set_xlabel('Velocity $v$ [m/s]')
ax.set_ylabel('Drag force $F$ [N]')
ax.grid(True)

# Plot the fitted function with high resolution
v_fit = np.linspace(np.min(measured_v), np.max(measured_v), 500)
F_fit = fit_function(v_fit, fit_b, fit_n)
ax.plot(v_fit, F_fit, '-', label='Fit')

# Plot the measured data with error bars
ax.errorbar(
    measured_v, measured_F,
    xerr=error_v, yerr=error_F,
    fmt='.', capsize=2, label='Data'
)

ax.legend()
plt.show()