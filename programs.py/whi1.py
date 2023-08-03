#prime number
n=int(input("enter a number:"))
count=0
i=2
while(i<=n//2):
    if(n%i==0):
        count=count+1
    i=i+1
if(count==0):
    print("prime number")
else:
    print("Not a prime")
    
