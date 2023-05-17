
def avg_area():
    shape=str(input("enter shape"))
    side=int(input("side of shape"))
    if shape=="rect":
        side2=int(input())
        print(side*side2,2*(side+side2))
    elif shape=="square":
        print("area is",side**2,"perimeter is",4*side)
    elif shape=="circle":
        print(3.14*(side**2),2*3.14*side)
        return 

def swap():
    x=int(input("input x for swap"))
    y=int(input("input y for swap"))
    x=x*y
    y=x/y
    x=x/y
    print("values of x,y are:",x,y)
    return
def change():
    t=int(input("temp in f"))
    temp_c=5/9*(t-32)
    print("temp in c",temp_c)
    return

    
avg_area()
