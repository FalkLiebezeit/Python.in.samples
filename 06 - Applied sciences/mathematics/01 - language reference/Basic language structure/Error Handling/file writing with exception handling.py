# Demonstration of file writing with exception handling in Python

try:
    # Open the file for writing (creates the file if it doesn't exist)
    fo = open("C:\\test2.txt", "w")
    fo.write("This is test file")
except IOError:
    print("Error: unable to find file or write data")
else:
    print("Data written to the file successfully")
finally:
    # Ensure the file is closed properly
    fo.close()