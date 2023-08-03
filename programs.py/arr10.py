from array import*
a=array('i',[])
n=int(input("enter the size of the array:"))
for i in range(0,n):
    a.append(int(input()))
#process
for i in range(0,n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
for i in a:
    print(i,end=" ")
