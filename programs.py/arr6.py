from array import*
a=array('i',[10,20,30,40,50])
for i in a:
    print(i,end=" ")
print()
x=int(input("enter a nuw element:"))
pos=int(input("enter position of the element:"))
a.insert(pos,x)
print()
print("\n now see this")
for i in a:
    print(i,end=" ")
#remove element
k=a.pop()
print()
print(k)
a.remove(10)
print()
for i in a:
    print(i,end=" ")

    
