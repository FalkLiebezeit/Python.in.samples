import numpy as np
import matplotlib.pyplot as plt

# Load data from a CSV file (online source)
arr = np.loadtxt(
    "https://raw.githubusercontent.com/swapnilsaurav/BookPythonAppsOnVSCode/main/HistogramData.csv",
    delimiter=",",
    dtype=float
)
print("Loaded data:")
print(arr)

# Create bins for the histogram (0, 10, 20, ..., 120)
bins = np.arange(0, 130, 10)

# Plot the histogram with labels and grid
plt.figure(figsize=(8, 4))
plt.hist(arr, bins=bins, color='skyblue', edgecolor='black')
plt.title("Histogram of Loaded Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()