#sortieren.py
#modul
def selectionSort(a):
    n=len(a)
    for i in range(n):
        k=i #Position links
        for j in range(i,n):
            if a[j]<a[k]:
                k=j
            a[i],a[k] = a[k],a[i]
    return a
#Sortieren durch Einfügen
def insertionSort(a):
    n=len(a)
    for i in range(n):
        temp=a[i]
        j=i
        while (j>0) and (a[j-1]) > temp:
            a[j]=a[j-1]
            j=j-1
            a[j]=temp
    return a

def bubbleSort(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j+1],a[j]=a[j],a[j+1]
    return a