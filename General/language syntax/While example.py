while True:
    """
    Infinite loop that continuously prompts the user for input until they type "quit".
    
    The input is processed in a case-insensitive manner using .lower().
    If the user enters "quit", the loop breaks and the program ends.
    Otherwise, the length of the input string is displayed.
    """

    s = input('Enter something: ')  # Prompt user for input

    if s.lower() == 'quit':  # Convert input to lowercase and check for exit condition
        break  # Exit loop if user types "quit"

    print("Length of the given text is", len(s))  # Display the length of the input string

print("Goodbye")  # Print farewell message after loop terminatesder dicke