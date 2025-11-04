# Linear Search Example
# Optimized and commented for clarity

def read_key():
    """
    Prompt the user to enter the key item to search for.
    Returns:
        int or float: The key item entered by the user.
    """
    try:
        key_item = float(input("Enter the key item to search: "))
        return key_item
    except ValueError:
        print("Invalid input. Please enter a number.")
        return read_key()

def linear_search(search_key):
    """
    Perform a linear search for search_key in the list ia.
    Prints the result and the location if found.
    """
    ia = [10, 20, 30, 40, 50]  # List to search
    n = len(ia)
    found = False

    # Iterate through the list to find the search_key
    for i in range(n):
        if ia[i] == search_key:
            found = True
            print('Item found at location', i + 1)
            break

    if not found:
        print("Item not found in the list")

def main():
    """Main function to run the linear search program."""
    key = read_key()
    linear_search(key)

if __name__ == "__main__":
    main()