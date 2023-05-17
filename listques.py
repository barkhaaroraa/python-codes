d=dict()
for i in range(5):
    a=int(input("enter key"))
    b=input("enter value")
    d[a]=b
print(d)
del d[8]
for x in d:
    print("key is ",x,"value is ",d[x])