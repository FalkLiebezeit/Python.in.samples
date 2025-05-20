# program E11x9.py
# appending to a file

def main():
    # open file for appending
    outfile = open("C:\\PythonFiles\\e2.txt", "a")
    outfile.write("appending fourth line\n")
    outfile.write('appending fifth line\n')
    outfile.close()
    # reading
    infile=open("C:\\PythonFiles\\e2.txt", 'r')
    print (infile.read())
    infile.close()

main()
