"""
Copilot:
Create a Python program that calculates Pi.

answer:
Here is a Python program that estimates the value of Pi using the Monte Carlo method, a widely used probabilistic technique:
"""

import random
import math

def estimate_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    return (inside_circle / num_samples) * 4

# Set the number of random points
num_samples = 1000000  # Increase for better accuracy
estimated_pi = estimate_pi(num_samples)

print(f"Estimated value of Pi after {num_samples} samples: {estimated_pi}")
print(f"Math module's Pi value: {math.pi}")