def fakultaet(n):
    if n==0:
        return 1
    else:
        return n*fakultaet(n-1)
    
fakultaet(5)