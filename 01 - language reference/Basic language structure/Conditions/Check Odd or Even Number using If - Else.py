# Check whether a given number is even or odd using if…else.

# --- Prompt user for input and convert to integer ---
number = int(input("Enter a number to check if even or odd: "))

# --- Check if the number is even or odd ---
if number % 2 == 0:
    print("....Inside if block....")
    print('It is an even number (divisible by 2).')
else:
    print("....Inside else block....")
    print('It is an odd number!')

print('Program ends here!')