l=[]
n=int(input("length of list"))
for x in range(n):
    a=int(input())
    l.append(a)
l[1:5]=[]
print("remove=[1:5]",l)
for x in range(n):
    a=int(input())
    l.append(a)
print(l)
l2=[]
for x in l:
    a=str(x)
    n=len(a)
    sum1=0
    for y in a:
        b=int(y)
        sum1=b+sum1
    l2.append(sum1)
print(sum1)
        
a=input("Enter string")
if a==a[::-1]:
    print("It is a palindrome")
else:
    print("Not palindrome")
a=['[1, 4, 5]', '[4, 6, 8]']
b=a.split(",")
print(b)
        
        
    


