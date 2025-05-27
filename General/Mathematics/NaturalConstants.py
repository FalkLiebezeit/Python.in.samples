"""
pip install scipy


Ki:

Write a Python program. 
The program should display all natural constants it knows. 
Optimize and comment the program.

"""

import scipy.constants as const

# Dictionary of important natural constants with their names as keys
constants = {
    "Speed of light in vacuum (m/s)": const.c,
    "Gravitational constant (m³ kg⁻¹ s⁻²)": const.G,
    "Planck constant (J·s)": const.h,
    "Reduced Planck constant (J·s)": const.hbar,
    "Elementary charge (C)": const.e,
    "Avogadro constant (mol⁻¹)": const.N_A,
    "Boltzmann constant (J/K)": const.k,
    "Gas constant (J/(mol·K))": const.R,
    "Fine-structure constant": const.alpha,
    "Electron mass (kg)": const.m_e,
    "Proton mass (kg)": const.m_p,
    "Neutron mass (kg)": const.m_n,
}

# Print each constant name along with its value
for name, value in constants.items():
    print(f"{name}: {value:.5e}")  # Format values for better readability

print("\n")