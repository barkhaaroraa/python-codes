
#for x in range(1,100):
        #if x%2==0:
                #print(x,"is even")
        #else:
                #print(x,"is odd")
#a=int(input())
#t=1
#for x in range(1,a+1):
        #t=t*x

        #print(t)
total=0
#for x in range(2,100,2):
        #total=total+x
#print(total)
#for x in range(1,100,2):
        #total=total+x
#print(total)
#for x in range(0,100):
        #if x%5==0:
                #print(x,"divisibleby 5")
        #else:
                #print(x,"not divisible")
#l=int(input())
#n=int(input())
#for x in range(0,l):
        #print(n,"x",x,"=",x*n)
#n=input()
b=0
#while n!=0:
        #a=n%10
        #n=n-a
        #n=n/10
        #b=b+a
#print("sum is",b)
#a=int(input())
#b=int(input())
#c=int(input())
#print(max(a,b,c))
#print(min(a,b,c))
a=["apple","banana","pear","strawberry","red","orange","mango","red","blue","fatfat","red","water","blue"]

count=0
#for i in a:
        #count1=0
      
        #if i=="red":
                #count=count+1
                #print(count)
#count = 0
#for ele in a: 
#if ele == "red":
        #count = count + 1
#print(count)
n=int(input())
number=1
d=1
fact=1
num=10
#for i in range(1,n+1):
        #number=number*i
#print(number)

def pnc():
        a=str(input("p or c  "))
        if a=="p" or a=="P":
                r=int(input("value for r"))
                number=1
                for i in range(1,n+1):
                        
                        number=number*i
                print("factorial of",n,"is",number)
                
                R=n-r+1
                d=1
                
                for x in range(1,R):
                        d=x*d
                print(d,"N-R!")
                ans=number/d
                print(ans,"permutation")
        elif a=="c":
                
                r=int(input("value of r!"))
                number=1
                for i in range(1,n+1):
                        
                        number=number*i
                print("factorial of",n,"is",number)
                R=n-r+1
                d=1
                for x in range(1,R):
                        d=x*d
                print("factorial of n-r",d)
                ans=number/d
                E=r+1
                num=1
                for y in range(1,E):
                        num=num*y
                print("factorial of r",num)
                final=ans/num
                print('C=',final)
        
                        
                
                
        
pnc()
pnc()

                
                                

        
      


