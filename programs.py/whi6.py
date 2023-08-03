#fabinocci series
n=int(input("enter a number:"))
n1=0
n2=1
n3=1
while(n3<=n):
    print(n3,end=" ")
    n1=n2
    n2=n3
    n3=n1+n2
    
