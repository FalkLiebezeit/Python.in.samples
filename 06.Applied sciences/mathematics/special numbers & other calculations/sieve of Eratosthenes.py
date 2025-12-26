"""Sieve of Eratosthenes: Efficient algorithm to find all prime numbers up to a given limit."""

import math
import numpy as np

# Upper limit (exclusive) for searching primes
upper_limit = 100

# Create a boolean array indicating potential primes.
# Start with all numbers marked as True (potential primes), except 0 and 1.
is_prime = np.ones(upper_limit, dtype=bool)
is_prime[:2] = False  # 0 and 1 are not primes

# Sieve process: mark multiples of each prime as False
for i in range(2, int(math.sqrt(upper_limit)) + 1):
    if is_prime[i]:
        # Mark all multiples of i (starting from i*i) as not prime
        is_prime[i * i : upper_limit : i] = False

# Extract the prime numbers using numpy's where function
primes = np.nonzero(is_prime)[0]

# Output the list of primes
print(primes)