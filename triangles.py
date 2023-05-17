# n=int(input())
# for x in range(0,n+1):
   
    
        
#     print(" "*x+"*"+"")   
#     #print("*")
   

# for x in range(0,n+2):
#     print("*",end="")

# print("\n",end="")
# for x in range(0,n+1):
#     for p in range(n-x,0,-1):
#         print(n-x,end="")
#     for j in range(0,x):
#         print(" "*2,end="")
#     for y in range(n-x,0,-1):
#         print(n-x,end="")
#     print("\n",end="")
# for x in range(0,n):
    
#     for y in range(n-x,0,-1):
#         print(" ",end="")
#     for t in range(0,1):
#         print("*",end="")
#     for j in range(1,x+2):
#         print(j,"*",end="")
#     print("\n",end="")

# for x in range(0,n):
#     for y in range(n-x,0,-1):
#         print(" ",end="")
#     for j in range(x+1,0,-1):
#         print(j,end="")
#     print("\n",end="")

# for x in range(0,n):
#     if x<=0:
#         print("*")
#     else:
    
   
#         print("*"+" "*x+"*")
#     print(end="")
# for x in range(0,n+2):
#     print("*",end="")
    
for inputt in range(100,500):
    number=inputt
    sum=0
    while number>0:
        d=number%10
        sum=sum+(d**3)
        number=number//10
    if inputt==sum:
        print("armstrongs number",inputt)
    else:
        continue
    