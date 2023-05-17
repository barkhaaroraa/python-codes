#question2
n=int(input())
for x in range(1,n):
    
    if x==1:
        print(x,end="")
    elif x%2==1:
        
        print(x+2,end="")
    else:
        print(x+1,end="")
    for y in range(1,x*2):
        
            print("#",end="")
    print()
#3
n="bluebells"
y=""

for x in n:
    y=y+x

    print(y)
    
#1
for x in range(1,n):
    for c in range(n,0,-1):
        print("_",end="")
    print()
   
    
