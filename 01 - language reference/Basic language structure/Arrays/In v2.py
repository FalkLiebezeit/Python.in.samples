# Check if the entered course is available in the list

# --- List of available courses ---
courses = ["C", "C++"]

# --- Prompt user for input ---
course = input("Enter the course: ")

# --- Check if the course is available ---
if course in courses:
    print("This course is available")
else:
    print("This course is not available")