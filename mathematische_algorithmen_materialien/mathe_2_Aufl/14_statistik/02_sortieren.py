#02_sortieren.py
def bubbleSort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j+1],a[j]=a[j],a[j+1]
                print(i,j,a)
         
def selectionSort(a):
    n=len(a)
    for i in range(n):
        k=i
        for j in range(i+1,n):
            if a[j]<a[k]:
                k=j
                a[i],a[k] = a[k],a[i]
                print(i,j,a)
    #return a
print("Bubble Sort")                
x=[5,4,3,2,1]
print("i","j",x)
print("--------------------")
bubbleSort(x)
print("Selection Sort")
x=[5,4,3,2,1]
print("i","j",x)
print("--------------------")
selectionSort(x)
