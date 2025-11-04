"""Calculation of the mean density of the Earth."""

import math

# Mean radius of the Earth in meters
R = 6_371_000
# Mass of the Earth in kilograms
mass = 5.972e24

# Calculate the volume of the Earth (assuming a sphere) in cubic meters
volume = (4 / 3) * math.pi * R**3

# Calculate the mean density in kg/m³
density = mass / volume

# Print the result in g/cm³ (1 kg/m³ = 0.001 g/cm³)
print(f"The mean density of the Earth is {density / 1e3:.3f} g/cm³.")