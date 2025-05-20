# program E11x1.py
# writing to a file

from pathlib import Path

#import os.path
import sys
def main(): '''definition of main function to write to a file.'''

file_path = Path('C:\\PythonFiles\\myfile.txt')

# check if file already exists
if not file_path.exists():
    print('filename does not exists')
    sys.exit()

else:
    # open file for writing
    outfile = open(file_path,"w")

    print('Writing')
   
    # writing lines to the file
    outfile.write('First line of Text\n')
    outfile.write('Second line of Text\n')
    outfile.write('Third Line of Text\n')
    outfile.close()  # close file after writing

    print('Done')

main()
