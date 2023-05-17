# for x in range(1,101):
#     if x%2==1:
#         print(x,"odd")
#     else:
#         print(x,"even")
# n=int(input())
# u=1
# print("factorial \n")
# for x in range(1,n+1):
#     u=u*x
# print(u)
# a=0
# b=0
# for x in range(1,n+1):
#     if x%2==1:
#         a=a+x
        
#     else:
        
#         b=b+x
# print(a,b)
# for x in range(1,51):
#     if x%5==0:
#         print(x,"is a multiple of 5")
#     else:
#         print(x,"is not a multiple of 5")
# k=0
# for x in range(1,11):
#     print(n,"x",x,"=",n*x)
# for x in range(10):
#     v=int(input())
#     k=k+v
# print(k)
# v=int(input())
# j=0
# for x in range(v,n):
#     if x%7==0:
#         j=x+j
# print(j)

# for x in range(1,n+1):
#     for y in range(1,x+1):
#         print(x,end="")
#     print("\n",end="")
    
h=input()
length=len(h)
for x in range(length-1,-1,-1):
    print(h[x],end="")

