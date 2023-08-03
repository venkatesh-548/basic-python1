from array import*
a=array('i',[])
n=int(input("enter how many elements do you want:"))
print("enter elements:")
for i in range(0,n):
    a.append(int(input()))
ele=int(input("enter the searching element:"))
i=0
flag=-1
while(i<n):
    if(ele==a[i]):
        flag=i
        print("the element found at",flag)
    i=i+1
if(flag==-1):
    print("element not found")
