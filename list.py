n=int(input())
a=[]
for c in range(n):
    v=int(input())
    a.append(v)
print(a)
sum1=0
for x in a:
    if x%15==0:
        sum1=x+sum1
print(sum1)


def digisum(n):
    a=len(n)
    b=int(n)
    sum1=0
    for x in range(a):
        c=b%10
        sum1=sum1+c
    return sum1
v=str(input())
print(digisum(v))
