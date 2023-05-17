# a=[]
# b=int(input("NO. OF ELEMENTS"))
# for x in range(1,b+1):
#     n=int(input())
#     a.append(n)
# print("list=",a)
# #a.insert(0,100)
# #print(a)

# a.reverse()
# print(a,"\n",len(a),a.count(int(input())))
# string1=input("string: ")
# subs=input("substring: ")
# length=len(string1)
# count=0
# lengthsubs=len(subs)
# for x in range(0,length-lengthsubs+1,1):
#     t=0
#     for y in range(0,lengthsubs):

#         if string1[x+y]!=subs[y]:
#             t=1
#             break
#     if t==0:
#         count+=1
        
        
# print(count)

string1=input()
string1=string1.lower()
length=len(string1)
dict={}
for x in string1:
    if x in dict:
        dict[x]=dict[x]+1
    else:
        dict[x]=1
for x in dict:
    print(x,": ",dict[x])
