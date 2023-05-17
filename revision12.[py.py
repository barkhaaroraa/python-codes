d={"hello":1,"rr":2,"yay":3}
n=input("key:")
for x in d:
    p=1
    if x==n:
        print(n,"is present")
        p=0
        break
if p==1:
    print(n,"not present")
        
d={}
for x in range(1,16):
    d[x]=x**2
print(d)


d1={1:33,2:55,5:55}
d2={1:66,6:33,7:44}
d1.update(d2)
print(d1)
d={1:11,6:55,9:22,3:33}
a=d.sorted()
print(a)

