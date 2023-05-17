l=[1,6,2,100,90,5,7,0]
for x in range(len(l)):
    while x>0:
        if l[x]>l[x-1]:
            l[x-1],l[x]=l[x],l[x-1]
            print(l)
        else:
            break
        x=x-1
print(l)      
        
        
