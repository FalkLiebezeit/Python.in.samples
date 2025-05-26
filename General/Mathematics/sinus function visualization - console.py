# Demonstration of a sinus function visualization

from math import cos, radians

# Function to create a string representation of a cosine wave in text form
def make_dot_string(x):
    """Generates a visual representation of cosine wave."""
    rad = radians(x)  # Convert degrees to radians for cosine function
    numspaces = int(20 * cos(rad) + 20)  # Scale result to fit within 0-40 spaces
    return ' ' * numspaces + 'o'  # 'o' represents the wave peak

def main():
    """Prints the cosine wave pattern from 0 to 1800 degrees."""
    for i in range(0, 1800, 12):  # Adjust step size for smoother visualization
        print(make_dot_string(i))

if __name__ == "__main__":
    main()