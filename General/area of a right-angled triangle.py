# Calculate the area of a right-angled triangle
def calculate_area(base: float, height: float) -> float:
    """Returns the area of a right-angled triangle given its base and height."""
    return 0.5 * base * height

def main():
    """Handles user input and displays the calculated area."""
    try:
        # Prompt user for input and ensure correct format
        user_input = input("Enter the base and height separated by a comma: ")
        base, height = map(float, user_input.split(','))

        # Validate input (ensure non-negative values)
        if base <= 0 or height <= 0:
            print("Error: Base and height must be positive values.")
            return

        # Calculate and display the area
        area = calculate_area(base, height)
        print(f"The area of the right-angled triangle is: {area:.2f} square units.")

    except ValueError:
        print("Invalid input. Please enter two numeric values separated by a comma.")

# Run the program
if __name__ == "__main__":
    main()