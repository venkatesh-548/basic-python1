n=int(input("enter n:"))
i=2
flag=0
while(i<=n):
    if(n%i==0):
        flag=1
        break
if(flag==0):
    print("prime number")
else:
    print("not prime")
    
