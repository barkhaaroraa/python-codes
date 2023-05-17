n=int(input())
if n%2==1:
    print("odd")
else:
    print("even")
if n>=18:
    print("eligible to vote")
else:
    print("not eligible")
a=str(input())

a.lower()
for v in a:
    if v=="a" or v=="e" :
        print(v,"beaking the flow")
        break
    else:
        print(v,"continued")
    
