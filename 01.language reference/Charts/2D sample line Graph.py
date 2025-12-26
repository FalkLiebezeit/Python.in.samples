import matplotlib.pyplot as plt

# --- Data for the line chart ---
x = [1, 2, 3, 4]         # X-axis values
y = [1, 16, 81, 256]     # Y-axis values

# --- Create the line plot ---
plt.figure(figsize=(8, 5))           # Set a larger figure size for better visibility
plt.plot(x, y, marker='o', linestyle='-', color='b', label='y = x^4')  # Add markers and label

# --- Add title and axis labels ---
plt.title("Sample Line Graph", fontsize=14, fontweight='bold')
plt.xlabel("X Value", fontsize=12)
plt.ylabel("Y Value", fontsize=12)

# --- Show legend and grid for clarity ---
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()