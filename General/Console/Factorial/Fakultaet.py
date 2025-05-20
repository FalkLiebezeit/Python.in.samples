# Demonstration of a recursion
# Author: Falk Liebezeit
# Date: 11-10-2019

#define function
def fak(n):
    if n > 0:
        return fak(n-1) * n
    else:
        return 1

#define main
def main():
    x = int(input("Geben Sie bitte eine Zahl ein: "))
    print(fak(x))
    return "Done!"

#run main
if __name__ == "__main__":
    main()
    