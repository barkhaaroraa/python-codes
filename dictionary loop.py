n=int(input("no. of students"))
a={}
for x in range(n):
    name=input("enter name")
    adm=int(input("admission no"))
    clss=input("class")
    per=int(input("PERCENTAGE"))
    a[adm]=name,clss,per
print(a)
chk=int(input("admission no."))


print(chk,a[chk])


