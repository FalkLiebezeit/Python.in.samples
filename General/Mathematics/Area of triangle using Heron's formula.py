# Calculate the area of a triangle using Heron's formula
import math

def calculate_triangle_area(a, b, c):
    """Calculates the area of a triangle given its three side lengths."""
    s = calculate_semi_perimeter(a, b, c)  # Calculate semi-perimeter
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Apply Heron's formula
    return area

def calculate_semi_perimeter(x, y, z):
    """Calculates the semi-perimeter of a triangle."""
    return (x + y + z) / 2

def main():
    """Main function to process user input and calculate the triangle's area."""
    side_a = int(input("Enter the length of the first side: "))
    side_b = int(input("Enter the length of the second side: "))
    side_c = int(input("Enter the length of the third side: "))  # Corrected variable name

    area = calculate_triangle_area(side_a, side_b, side_c)
    print(f"\nThe area of the triangle is: {area:.2f}\n")

# Start the program
if __name__ == "__main__":
    main()