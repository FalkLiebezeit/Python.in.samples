# global and local scope
X = 5
# Uses global because there is no local 'X'
def fun1():
    print('Inside fun1() : ', X)
# Variable 'X' is redefined as a local
def fun2():   
    X = 7
    print( 'Inside fun2() : ',X)
# Uses global keyword to modify global 'X'
def fun3():
    global X 
    X = 9
    print('Inside fun3() : ',X)
def main():
    print ('global : ',X)
    fun1()
    print ('global : ',X)
    fun2()
    print ('global : ',X)
    fun3()
    print ('global : ',X)

main()
