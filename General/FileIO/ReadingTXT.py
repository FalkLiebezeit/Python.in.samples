# program E11x2.py
# reading from a file

file_path = 'C:\\PythonFiles\\myfile.txt'


def main():
    # open file for reading
    infile = open(file_path, "r")
    
    # reading
    print (infile.read())
    # close file

main()
