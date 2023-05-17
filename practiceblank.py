n=int(input())
for x in range(n):
     for z in range(n-x):
          print(" ",end="")
     for y in range(x):
          print("*",end="")

     for u in range(x-1):
          print("*",end="")
     
     print("")
          
for x in range(n):
     for p in range(x):
          print(" ",end="")
     for q in range(n-x):
          print("*",end="")
     for r in range(n-x-1):
          print("*",end="")
     
     
     
     
     print("")
          
