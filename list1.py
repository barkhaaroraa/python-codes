s="123hello world123"
a=[]
b=[]
c=[]
for x in s:
    if x.isalpha()==True:
        a.append(x)
    elif x.isnumeric():
        b.append(x)
    else:
        c.append(x)
        
print(a)
print(b)
       
num = input("Enter ASCII value: ")
print(chr(num))
