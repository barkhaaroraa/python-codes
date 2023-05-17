n=int(input())
l=[]
for x in range(n):
    a=int(input())
    l.append(a)

print(l)
sumo=0
count=0
sume=0
for x in l:
    if x%2==1:
        sumo=sumo+x
        count=count+1
    else:
        sume=sume+x
print(count,"no of odd nos \n","sum of odd nos",sumo,"\n","sum of even nos",sume)
