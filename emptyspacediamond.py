n=int(input())
def end9():
    for x in range(1,n):
        for y in range(x,n):
            print(y,end="")
        for y in range(1,x):
            print(" "*2,end="")
        for y in range(1,n-x+1):
            print(y,end="")
        
        print("\n",end="")
            



def end1():
    
    for x in range(1,n):
        for y in range(n-1,n-x-1,-1):
            print(y,end="")
        for y in range(x+1,n):
            print(" "*2,end="")
        for y in range(x,0,-1):
            print(y,end="")
        
        print("\n",end="")
        


end9()
end1()
##for x in range(1,n):
        #for y in range(1,x+1):
            #print(y,end="")
        #for y in range(x+1,n):
            #print(" "*2,end="")
        #for y in range(n-1,n-x-1,-1):
            #print(y,end="")
        #
        
    
