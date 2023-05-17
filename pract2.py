n=int(input())
for x in range(1,n+1):
    if x==1:
        print("*",end="")
        
    else:
        print("*"+" "*(x-1)+"*",end="")
    print("\n",end="")
for x in range(1,n+3):
    print("*",end="")

u=int(input())
y=u+1


for x in range(1,y):
    d=str(x)
    if len(d)==2 or len(d)==1:
        
        a=x%10
        if x%10==0:
            
            continue 
        elif x/a==a:
            print(x,"is a square of",a)
            continue
    
        else:
            
            continue
    
    
    elif len(d)==3:
        
        a=x%100
    if x%100==0:
        continue 
    elif x/a==a:
        print(x,"is a square of",a)
    
    else:
        continue


