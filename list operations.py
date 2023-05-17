l=[1,2,3,-4,-6,-2,-7,9,4,6]
l2=[]
for x in range(len(l)):
    if l[x]>0 and l[x]%2==0:
        l2.append(l[x])
print(l2)
n=int(input("no search"))

a="not present"
for x in range(len(l)):
    if l[x]==n:
        a="present"
        break
        
print(a)
l1=[1,2,3,4,5,7,10,11,16,21,45,15]
list2=[]
##for x in l1:
 #   if x%5==0:
 #       list2.append(x+5)
    
  #  if x%10!=0 and x%10!=5:
  #      list2.append(x+10)
#print(list2)




for x in l1:
    sum1 = 0
    if x%3 == 0:
        sum1 += 3
    if x%5 ==0:
        sum1+=5
    list2.append(x+sum1)
list3=[1,2,3,4,5,6,6,6,3,2]
l=len(list3)
l1=int((l/2))
list2=list3[:l1]
#print(list2)

list4=list3[l1:]
finallist=list4+list2
#print(finallist)

list3=[1,2,3,4,4]
duplicate=[]
unique=[]
for x in list3:
    if list3.count(x)==1:
        unique.append(x)
    elif list3.count(x)>1:
        duplicate.append(x)
print(duplicate,unique)
a=["Hello","America","aus","world","CS"]
b=[]
for x in a:
    if x[0]=='a' or x[0]=='A':
        b.append(x)
print(b)
lis=["hello","world",13,43,77,23,65,"abc",1.3]
sum1=0
for x in lis:
    if type(x)==str:
        continue
    elif type(x)==int or type(x)==float:
        if x%10==3:
            sum1=sum1+x
        else:
            continue
print(sum1)
num=[3,21,5,6,14,8,14,3]
for x in range(-1,-(len(num)),-1):
    if num[x]%7==0:
        num[x],num[x+1]=num[x+1],num[x]
        
print(num)
            
