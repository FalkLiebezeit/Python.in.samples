# Calculate the gravitational force between a 90 kg body and the Earth

# --- Constants ---
G = 6.67430e-11          # Gravitational constant in m^3 kg^-1 s^-2
mass_earth = 5.972e24    # Mass of the Earth in kg

# --- Given values ---
m1 = 90                  # Mass of the first body in kg
m2 = mass_earth          # Mass of the Earth in kg
r = 6378e3               # Distance between centers (Earth's radius) in meters

# --- Calculate gravitational force using Newton's law ---
# Formula: F = G * (m1 * m2) / r^2
F = G * (m1 * m2) / r**2

# --- Output the result ---
print(f"The gravitational force between the 90 kg body and the Earth is {F:.2f} N")

# Comments:
# - G is the universal gravitational constant.
# - m1 is the mass of the body (90 kg).
# - m2 is the mass of the Earth.
# - r is the distance between the centers (Earth's radius).
# - The result is printed with two decimal places for clarity.