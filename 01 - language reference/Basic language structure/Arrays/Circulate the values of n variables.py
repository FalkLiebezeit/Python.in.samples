# Circulate the values of n variables in a list

def circulate(lst):
    """
    Circulates the values in the list by moving the first element to the end,
    and prints the list after each circulation.
    """
    n = len(lst)
    for i in range(n):
        elem = lst.pop(0)      # Remove the first element
        lst.append(elem)       # Append it to the end
        print(f"Circulated list after {i+1} step(s): {lst}")

def main():
    # --- Input: number of elements ---
    try:
        no_of_elements = int(input("Enter number of values: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    # --- Input: elements of the list ---
    lst = []
    for i in range(no_of_elements):
        while True:
            try:
                elem = int(input(f"Enter integer {i+1}: "))
                lst.append(elem)
                break
            except ValueError:
                print("Please enter a valid integer.")

    print('Original sequence is:')
    print(lst)

    # --- Circulate and display the list ---
    circulate(lst)

if __name__ == "__main__":
    main()