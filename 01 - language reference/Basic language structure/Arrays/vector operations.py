import numpy as np

# --- Define two numpy arrays (vectors) ---
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

# --- Output the vectors ---
print("Vector      A:", A)
print("Vector      B:", B)

# --- Vector addition ---
print("Sum       A+B:", A + B)

# --- Element-wise product ---
print("Product   A*B:", A * B)

# --- Cross product (vector product) ---
print("Cross product   :", np.cross(A, B))

# --- Dot product (scalar product) ---
print("Dot product     :", np.dot(A, B))