# Recursive Factorial

""" old function name
def factpld(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factold(n-1)
"""
   


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)




def main():
    num=eval(input("Enter the number whose factorial to be found "))
    print('factorial of', num, '=', fact(num))

main()
