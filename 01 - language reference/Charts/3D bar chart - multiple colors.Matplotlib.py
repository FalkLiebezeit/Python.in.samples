import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

# --- Set font weight for y-axis labels ---
rc('font', weight='bold')

# --- Data for each quarter (in thousand Crores) ---
Y22Q1 = [11, 14, 10, 18, 13]   # Q1 values
Y22Q2 = [17, 21, 19, 8, 11]    # Q2 values
Y22Q3 = [36, 22, 3, 16, 34]    # Q3 values

# --- Bar positions and labels ---
cities = ['Mumbai', 'Delhi', 'Hyderabad', 'Kolkata', 'Chennai']
x = np.arange(len(cities))      # Bar positions on x-axis
bar_width = 0.8                 # Bar width for better appearance

# --- Calculate cumulative heights for stacking ---
bottom_q2 = Y22Q1
bottom_q3 = np.add(Y22Q1, Y22Q2)

# --- Plot stacked bars for each quarter ---
plt.bar(x, Y22Q1, color='#7f6d5f', edgecolor='white', width=bar_width, label='Q1')
plt.bar(x, Y22Q2, bottom=bottom_q2, color='#557f2d', edgecolor='white', width=bar_width, label='Q2')
plt.bar(x, Y22Q3, bottom=bottom_q3, color='#2d7f5e', edgecolor='white', width=bar_width, label='Q3')

# --- Custom X axis and labels ---
plt.xticks(x, cities, fontweight='bold')
plt.xlabel("Cities", fontweight='bold')
plt.ylabel("in thousand Crores", fontweight='bold')
plt.title("Quarterly Average GST Collection", fontweight='bold')
plt.suptitle("Top 5 Cities in India", fontweight='bold')
plt.legend(title="Quarter")

# --- Improve layout and show plot ---
plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust layout to fit suptitle
plt.show()