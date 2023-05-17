def bubblesort(a):
    n=len(a)
    for x in range(0,n):
        swap=False
        for y in range(0,n-1-x):
            if a[y]>a[y+1]:
                a[y],a[y+1]=a[y+1],a[y]
                swap=True
                
                
        if swap==False:
            break
    return a

l=[]
b=int(input())
for e in range(b):
    n=int(input())
    l.append(n)
print(l)

print(bubblesort(l))
