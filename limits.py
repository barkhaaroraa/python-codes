l=int(input())
n=int(input())
for x in range(0,l):
        print(n,"x",x,"=",x*n)
        
l=int(input())
inputs=[]
for i in range(0,l):
    
    inputs.append(float(input("enter no ")))    
    SUM=sum(inputs)
    avg=float(SUM/l)

print(SUM,avg)
   
