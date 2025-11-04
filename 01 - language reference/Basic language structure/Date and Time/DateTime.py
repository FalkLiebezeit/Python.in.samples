"""Format and print a date with ordinal suffixes for the day."""

# List of month names
months = [
    'January', 'February', 'March',
    'April', 'May', 'June',
    'July', 'August', 'September',
    'October', 'November', 'December'
]

# List of ordinal endings for days (1st, 2nd, 3rd, 4th, ..., 31st)
endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']

# Prompt user for year, month, and day
year = input("Enter Year: ")
month = int(input("Enter Month (1-12): "))
day = int(input("Enter Day (1-31): "))

# Get the month name and day with ordinal ending
month_name = months[month - 1]
day_with_ending = str(day) + endings[day - 1]

# Print the formatted date
print(f"The date you have entered is {day_with_ending} {month_name} {year}")