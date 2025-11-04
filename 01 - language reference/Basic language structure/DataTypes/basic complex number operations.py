"""Demonstration of basic complex number operations in Python."""

# Define a complex number and a real number
x = 5.0 + 4.5j
y = 2.0

# Perform arithmetic operations and print results
print("x + y =", x + y)         # Addition
print("x - y =", x - y)         # Subtraction
print("x * y =", x * y)         # Multiplication

# Print real and imaginary parts of x
print("Real part of x:", x.real)
print("Imaginary part of x:", x.imag)

# Print the complex conjugate of x
print("Conjugate of x:", x.conjugate())