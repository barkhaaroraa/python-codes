l=[1,1,1,1,3,3,3,3,3,5,5,9,8,8,6]
d={}
for x in l:
    current_freq = d.get(x, 0)
    d[x] = current_freq + 1

print(d)
    
for x in d:
    a="largest"
    for y in d:
        if d[x]<d[y]:
            a="smallest"
        continue
    if a=="largest":
        print(x,":",d[x])
    
v=min(d.values())
for y in d:
    if d[y]==v:
        print(y,":",d[y])

for x in d:
    if d[x]%2==0:
        print(x,":",d[x]," ",end="")
d={}
d["a"]=0
d["e"]=0
d["i"]=0
d["o"]=0
d["u"]=0
freq=0
for x in a:
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
        freq=d.get(x,0)
        d[x]=freq+1
        print(x)
print(d)
d={}
for x in range(2):
    name=input("enter name \t")
    basic=int(input("basic salary"))
    rent=int(input("rent"))
    conv=int(input("conv"))
    d[name]=[basic,rent,conv]
k=d.keys()
for x in k:
    print(x,d[x],"salary",sum(d[x]))
n=input("name")
for x in d:
    if x==n:
        print(x,d[x])
    

