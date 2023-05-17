n=int(input())
p=n
for q in range(p):
    for s in range(p-q):
        print(" ",end="")
    for r in range(1,q+1):
        print(r,end="")
    for t in range(q-1,0,-1):
        print(t,end="")
    print("\n",end="")
for x in range(n):
    for a in range(x):
        print(" ",end="")
    for y in range(1,n-x):
        print(y,end="")
    for b in range(n-x,0,-1):
        print(b,end="")
    print("\n",end="")

    
    
