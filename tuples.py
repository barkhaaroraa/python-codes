n=3
d={}
for x in range(n):
    name=input("name:")
    items=int(input("no. of items:"))
    phone=int(input("phone no:"))
    cost=int(input("total cost"))
    d[name]=[items,phone,cost]
print(d)
print("name\t","items\t","phone\t","cost\t")
for x in d:
    print(x,"\t",d[x][0],"\t",d[x][1],"\t",d[x][2])
    
