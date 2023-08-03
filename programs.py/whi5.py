#perfect number==)sum of factors=num
n=int(input("enter a number:"))
sum=0
i=1
while(i<n):
    if(n%i==0):
        sum=sum+i
    n=i+1
if(sum==n):
    print("perfect number")
else:
    print(" not a perfect number")

    
