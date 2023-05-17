

# for x in range(1,10):
#     for y in range(1,x+1):
#         print(x*y," ",end="")
#     print("\n",end="")


stringg="khokho"
def symmatric(stringg):
    length=len(stringg)
    begin=0
    last=length-1
    mid=length//2
    val=1
    # print(length//2)
    while(begin<mid and mid<=last):
        if(stringg[begin]==stringg[mid]):
            begin=begin+1
            mid=mid+1
        else:
            val=0
    if(val==1):
        print("is symmatric")
    else:
        print("nope")



def palindrome(stringg):
    length=len(stringg)
    begin=0
    last=length-1
    mid=length//2
    val=1
    while(begin<=mid and last>=mid):

        if(stringg[begin]==stringg[last]):
            begin=begin+1
            last=last-1
        else:
            val=0
            
    if(val==1):
        print("is palindrome")
palindrome(stringg)
symmatric(stringg)