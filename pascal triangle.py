def pascal(n):
        for x in range(1,n+1):
            for y in range(n-x):
                print(" ",end="")   #inverted triangle blank spaces
            for z in range(1,x):
                print(z,end="")     #normal counting
            for q in range(x,0,-1):
                print(q,end="")       #backward counting 
            
            print("\n",end="")
        
            
        
pascal(5)
    
