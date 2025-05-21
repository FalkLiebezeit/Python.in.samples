# Calculate the area of a right-angled triangle

def calculate_area(base, height):
    """Calculates the area of a right-angled triangle."""
    return 0.5 * base * height

def main():
    """Main function to handle user input and display the calculated area."""
    try:
        # Prompting the user to enter base and height values separated by a comma
        base, height = map(float, input("Enter the base and height separated by a comma: ").split(','))

        # Calculating and displaying the area
        area = calculate_area(base, height)
        print(f"The area of the right-angled triangle is: {area:.2f}")

    except ValueError:
        print("Invalid input. Please enter two numeric values separated by a comma.")

# Run the program
if __name__ == "__main__":
    main()