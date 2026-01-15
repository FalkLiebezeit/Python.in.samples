def fakultaet(n):
    print(n)
    if n==0:return 1
    else:
        zw = n*fakultaet(n-1);print(n," ",zw)
        return zw
fakultaet(5)




'''
5*(4*(3*(2*(1*fakultaet(0)))))
'''
