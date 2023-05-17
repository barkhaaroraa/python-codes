def index1(t,l1):
    for x in l1:
        index2=-1
        for y in range(0,len(l1)-1):
            if l1[y]==t:
                index2=y
                break
            
    return index2
n=int(input("length of list"))
m=[]
for i in range(1,n+1):
    o=int(input("list"))
    m.append(o)
y=int(input("target"))
print(index1(y,m))
