import numpy as np

# --- Create a 3D numpy array ---
array = np.array([
    [[1, 3, 5], [2, 4, 6]],    # First 2x3 matrix
    [[3, 2, 1], [1, 2, 3]]     # Second 2x3 matrix
])

# --- Output the number of dimensions ---
print("Number of dimensions:", array.ndim)

# --- Output the shape of the array for clarity ---
print("Shape of the array:", array.shape)

# --- Output the 3D array itself ---
print("3D array:\n", array)