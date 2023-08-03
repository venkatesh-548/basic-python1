#armstrong number
n=int(input("enter a number:"))
s=n
sum=0
while(n>0):
    num=n%10
    sum=sum+(num*num*num)
    n=n//10
if(s==sum):
    print("armstrong number")
else:
    print("not an armstrong")
