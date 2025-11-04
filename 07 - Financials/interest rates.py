"""
A sum of €88,000 is expected to grow to €150,000 in 10 years.
Calculate the interest rate required for this.

"""

"""
A sum of €88,000 is expected to grow to €120,000 in 10 years.
Calculate the interest rate required for this and show the growth in a diagram.
"""

import matplotlib.pyplot as plt
import numpy as np

# --- Given values ---
present_value = 88000      # Initial amount in euros
future_value = 150000     # Desired amount in euros
years = 10                 # Number of years

# --- Calculate the required annual interest rate ---
rate = (future_value / present_value) ** (1 / years) - 1

print(f"Required annual interest rate: {rate * 100:.2f}%")

# --- Calculate the value for each year ---
year_list = np.arange(0, years + 1)
values = present_value * (1 + rate) ** year_list

# --- Plot the growth ---
plt.figure(figsize=(8, 5))
plt.plot(year_list, values, marker='o', color='blue', label='Investment Growth')
plt.title("Investment Growth Over Time")
plt.xlabel("Years")
plt.ylabel("Value (€)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(year_list)
plt.legend()
plt.tight_layout()
plt.show()