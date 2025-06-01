from array import *


def main():

    a1=array('i',[12, 18, 6, 24, 72])    # Integer array declared

    print('\noriginal array is: ', a1)

    total = 0  # Variablenname „sum“ ist ungünstig, da es eine eingebaute Funktion gibt

    for x in a1:
        total += x 
        print(x,' : ', total)
       

    print('\nsum=', sum)

    
main()
