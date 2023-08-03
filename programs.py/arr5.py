from array import*
a=array('i',[])
#getting elements from keyboard at runtime
i=1
while(i<=5):
    x=int(input("enter elements:"))
    a.append(x)
    i=i+1
print()
ele=int(input("enter the searching element:"))
loc=a.index(ele)
print("the location is:",loc)
