import numpy as np  # Import NumPy for matrix operations

# Define coefficient matrix A (system of equations)
A = np.array([
    [2, 5, 2], 
    [3, -2, 4], 
    [-6, 1, -7]
])

# Print the coefficient matrix (optional)
print("Coefficient Matrix A:\n", A)

# Define constant matrix b (right-hand side values of equations)
b = np.array([[-38], [17], [-12]])

# Print the constant matrix (optional)
print("Constant Matrix b:\n", b)

# Compute the determinant of A to check if the system has a unique solution
det_A = np.linalg.det(A)

if det_A == 0:
    print("Solution is not possible! (Singular matrix)")
else:
    # Compute the inverse of A
    A_inv = np.linalg.inv(A)

    # Solve the system using matrix multiplication (Ax = b ⟹ x = A⁻¹ * b)
    solution = np.matmul(A_inv, b)

    # Print formatted solution (extract values properly)
    print("Solution: x = {:.2f}, y = {:.2f}, z = {:.2f}".format(solution[0, 0], solution[1, 0], solution[2, 0]))