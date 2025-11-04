def menu():
    """
    Display the calculator menu and return the user's choice.
    """
    print("Your options are:\n")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Quit\n")
    return input("Choose your option: ")

def add(a, b):
    """Add two numbers and print the result."""
    print(f"{a} + {b} = {a + b}")

def sub(a, b):
    """Subtract two numbers and print the result."""
    print(f"{a} - {b} = {a - b}")

def mul(a, b):
    """Multiply two numbers and print the result."""
    print(f"{a} * {b} = {a * b}")

def div(a, b):
    """Divide two numbers and print the result. Handles division by zero."""
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"{a} / {b} = {a / b}")

def get_number(prompt):
    """
    Prompt the user for a number and validate input.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    """
    Main loop for the calculator program.
    """
    while True:
        choice = menu()
        if choice == '1':
            a = get_number("Add this: ")
            b = get_number("to this: ")
            add(a, b)
        elif choice == '2':
            a = get_number("Subtract this: ")
            b = get_number("from this: ")
            sub(a, b)
        elif choice == '3':
            a = get_number("Multiply this: ")
            b = get_number("by this: ")
            mul(a, b)
        elif choice == '4':
            a = get_number("Divide this: ")
            b = get_number("by this: ")
            div(a, b)
        elif choice == '5':
            print("Thank you!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 5.")

if __name__ == "__main__":
    main()