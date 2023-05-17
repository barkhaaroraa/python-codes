a=[]
n=int(input())
for x in range(n):
    u=int(input())
    a.append(u)
print(a)
for x in range(len(a)-1):
    if a[x]%2==1 and a[x+1]%2==0:
        
            
        print("first loop")
            
        a[x],a[x+1]=a[x+1],a[x]
        print(a)
    if a[x]%2 ==0 and a[x+1]%2==1:
        
        
            
        a[x],a[x+1]=a[x+1],a[x]
        print(a)
            
        
print(a)
for c in range(len(a)):
    greatest=False
    
    for d in range(len(a)):
        greatest=False
        if a[c]>a[d]:
            greatest=True
                    
        
    if greatest==True:
        print("index",e,"no.")
        
