#concatination of two arrays
from array import*
a=array('i',[])
b=array('i',[])
i=1
#getting 1st array elements
while(i<=10):
    x=int(input("enter elements:"))
    a.append(x)
    i=i+1
print()
#getting second array elements
i=1
while(i<=10):
    x=int(input("enter elements:"))
    b.append(x)
    i=i+1
print()
#concastination
a.extend(b)
for i in a:
    print(i,end=" ")

    
