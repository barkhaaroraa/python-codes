n=str(input("enter sentence"))
for i in n:
    if i==" ":
        i="*"
        print(i,end='')
    else:
        print(i,end="")
print("\n",end="")  
for u in n:
    print(ord(u)," ",end="")
    
