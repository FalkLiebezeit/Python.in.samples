"""Demonstration of basic dictionary operations in Python."""

# Create a dictionary with initial key-value pairs
my_dict = {
    "name": "Snehil Saurav",
    "age": 27,
    "country": "UK"
}

# Accessing dictionary items
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("Country:", my_dict["country"])

# Adding an item
my_dict["gender"] = "Male"

# Removing an item
del my_dict["age"]

# Looping through the dictionary and printing key-value pairs
for key, value in