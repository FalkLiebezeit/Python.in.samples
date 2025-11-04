"""
Calculate the gravitational force between two bodies. 
One body weighs 100 kg, the other 200 kg. 
The distance is 1000 m. 
Optimize and annotate in English.

"""

# Calculate the gravitational force between two bodies using Newton's law of universal gravitation

# --- Constants ---
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2

# --- Given values ---
m1 = 100    # Mass of the first body in kg
m2 = 200    # Mass of the second body in kg
r = 1000    # Distance between the centers of the masses in meters

# --- Calculate gravitational force ---
# Formula: F = G * (m1 * m2) / r^2
F = G * (m1 * m2) / r**2

# --- Output the result ---
print(f"The gravitational force between the two bodies is {F:.6e} N")

# Comments:
# - G is the universal gravitational constant.
# - m1 and m2 are the masses of the two bodies.
# - r is the distance between the centers of the two masses.
# - The result is printed in scientific notation for