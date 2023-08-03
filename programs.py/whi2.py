#sum of digits
n=int(input("enter a n:"))
sum=0
while(n>0):
    num=n%10
    sum=sum+num
    n=n//10
print("the sum of digits is",sum)
