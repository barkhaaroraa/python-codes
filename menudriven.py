print("for diamond pattern press 1")

print("for finding a no. in list press 2")

print("for hollow triangle press 1")
u=int(input("1,2,3"))








if u==1:
    n=int(input("counting"))
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
elif u==2:
    n=int(input("input no"))
    x=[]
    i=0

    for u in range(1,n):
        a=int(input())
        x.append(a)
    print(x)
    a=0
    g=0

    s=int(input("find"))
    for w in x:
        g=g+1
    
        if s==x[g-1]:
        
            a=a+1
    print(s,"is present in the list",a,"no of times")
    
    print("max=",max(x))
    print("min=",min(x))
elif u==3:
    
    n=int(input())
    for x in range(1,n+1):
        if x==1:
            print("*",end="")
        
        else:
            print("*"+" "*(x-1)+"*",end="")
        print("\n",end="")
    for x in range(1,n+3):
        print("*",end="")
else:
    print("function not found:((")


    
    
