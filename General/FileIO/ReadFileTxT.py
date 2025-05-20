# program E11x7.py
# implicit method for reading

"""Definition of main function to read from a file."""
def main():

    # open file for reading
    infile = open('C:\\PythonFiles\\myfile.txt', "r")
    # reading
    for line in infile:
        print (line)
    # closing file

main()
