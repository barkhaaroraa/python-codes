
n=int(input())
a=[]
for x in range(n):
    s=int(input())
    a.append(s)
print(a)

def bubblesort(l):
    for x in range(len(l)-1):
        for y in range(len(l)-x-1):
            if l[y]<=l[y+1]:
                l[y],l[y+1]=l[y+1],l[y]
            else:
                continue
    return l

bubblesort(a)
print("sorted list=",a)
