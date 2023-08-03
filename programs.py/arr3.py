from array import*
a=array('i',[])
for i in a:
    print(i,end=" ")


#getting elements from keyboard
i=1
while(i<=10):
    x=int(input("enter values:"))
    a.append(x)
    i=i+1
print()

k=array('i',[1,2,3,4,1,1,1,4,5,6,7,1,1,1])
print("no of 1's in array:",k.count(1))
