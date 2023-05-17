d={}
nd={}
n=int(input("enter the no. of students"))
for x in range(n):
    a=int(input("enter admission no"))
    b=input("enter name")
    c=input("enter class and section")
    e=input("enter stream")
    d[a]=b,c,e
print(d)

find=int(input("enter roll no to be searched"))
for c in d:
    print("adm no. to be searched",find)
    if c==find:
        
        print("you wish to delete or update or no change?")
        choice=input("del or update or none for no change")
        if choice.lower()=="del":
            del d[c]
            print("final records available:",d)
            break
            
        elif choice.lower()=="update":
            b=input("enter new name")
            c=input("enter new class and section")
            e=input("enter new stream")
            nd[c]=b,c,e
        
        else:
            nd[c]=d[c]
        print("name\t","class\t","stream\t")
        for y in nd[c]:
            print(y,"\t",end="")
        break
        
    else:
        print("admission no. not found")

