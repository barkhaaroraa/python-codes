n=int(input())
for x in range(n+2):
    for y in range(x+1):
        print(" ",end="")
    for z in range(n+1):
        print(2*"v",end="")
    for a in range(n-x,-1,-1):
        print(" ",end="")
    for b in range(n-x-1,-1,-1):
        print(" ",end="")
    for c in range(n+1):
        print(2*"v",end="")
    print("\n",end="")
print("\n",end="")

for x in range(n//2+1):
    for y in range(5*n):
        print("e",end="")
    print("\n",end="")
for x in range(n//2):
    for y in range(2*n):
        print("e",end="")    
    print("\n",end="")
for x in range(n//2+1):
    for y in range(5*n):
        print("e",end="")
    print("\n",end="")
for x in range(n//2):
    for y in range(2*n):
        print("e",end="")    
    print("\n",end="")
for x in range(n//2+1):
    for y in range(5*n):
        print("e",end="")
    print("\n",end="")

print("\n",end="")
for x in range(n-1):
    print(5*"D",end="")
print("\n",end="")
for x in range(n):
    print(5*"D",end="")
    for y in range(n-1):
        print(4*" ",end="")
    print("D",end="")
    print("\n",end="")
for x in range(n-1):
    print(5*"D",end="")
