"""
# This program calculates the variance, standard deviation, and arithmetic mean of 
   screw lengths, and displays the frequency distribution in a graph.
 
   https://www.mathe-lerntipps.de/standardabweichung/
 
 Write a Python program for the following task:

A company manufactures screws that are 70 mm long.

To check the quality of the production, 80 screws were taken and their lengths were measured.

The result can be seen in the following table:

Length [mm] 69.6 69.7 69.8 69.9 70 70.1 70.2 70.3 70.4
Frequency 1 3 7 13 19 16 13 6 2

Display the length and frequency in a graph.

Determine the variance, the standard deviation, and the arithmetic mean including the standard deviation.
"""



import numpy as np
import matplotlib.pyplot as plt


# --- Measured screw lengths and their frequencies ---
lengths = np.array([69.6, 69.7, 69.8, 69.9, 70.0, 70.1, 70.2, 70.3, 70.4])
frequencies = np.array([1, 3, 7, 13, 19, 16, 13, 6, 2])



# --- Expand the data to a full sample for statistics ---
sample = np.repeat(lengths, frequencies)

# --- Calculate statistics ---
mean = np.mean(sample)
variance = np.var(sample, ddof=1)  # Sample variance
std_dev = np.std(sample, ddof=1)   # Sample standard deviation

# --- Output the results ---
print(f"Arithmetic mean: {mean:.3f} mm")
print(f"Variance: {variance:.5f} mm²")
print(f"Standard deviation: {std_dev:.5f} mm")
print(f"Mean ± Std Dev: {mean:.3f} ± {std_dev:.3f} mm")

# --- Plot the frequency distribution ---
plt.figure(figsize=(8, 5))
plt.bar(lengths, frequencies, width=0.07, color='skyblue', edgecolor='black')
plt.xlabel("Length [mm]")
plt.ylabel("Frequency")
plt.title("Frequency Distribution of Screw Lengths")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


# --- End of the program ---