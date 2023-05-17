from tkinter.font import nametofont


st=[]
def push(n):
    st.append(n)
    return st
while len(st)<5:
    n=input()

    push(n)
print("stack overflow")
for x in range(len(st)-1,-1,-1):
    print(st[x])