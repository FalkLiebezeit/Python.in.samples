# Demonstration of Bitwise Operators
a = 10  
b = 4  

print(a & b)  # Bitwise AND: Only the bits set in both numbers remain
# Output: 0 (0000 0000)  

print(a | b)  # Bitwise OR: Bits set in either number are kept
# Output: 14 (0000 1110)  

print(a ^ b)  # Bitwise XOR: Bits set in one number but not both
# Output: 14 (0000 1110)  

print(~a)  # Bitwise NOT: Flips all bits (2’s complement representation)
# Output: -11  

# Bitwise Right Shift (>>) for unsigned numbers:
# Shifts bits to the right, dividing by powers of two
a = 10  # Binary: 0000 1010  
print(a >> 1)  # Shifts bits right by 1 position
# Output: 5 (0000 0101)  

print(a >> 2)  # Shifts bits right by 2 positions
# Output: 2 (0000 0010)  

# Bitwise Right Shift (>>) for signed numbers using 2’s complement:
# Preserves sign bit during shifting
a = -10  
print(a >> 1)  
# Output: -5  

print(a >> 2)  
# Output: -3  

# Bitwise Left Shift (<<): 
# Shifts bits to the left, multiplying by powers of two
c = 5  # Binary: 0000 0101  
print(c << 1)  # Shifts bits left by 1 position (multiplying by 2)
# Output: 10  

print(c << 2)  # Shifts bits left by 2 positions (multiplying by 4)
# Output: 20  

d = -10  # Negative number shifting maintains sign
print(d << 1)  
# Output: -20  

print(d << 2)  
# Output: -40  