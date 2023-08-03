#fiding sum an davg of marks using array
str=input("enter subject marks with spaces:").split(' ')
print(type(str))
print(str)
marks=[int(num) for num in str]
print(marks)
c=0
sum=0
for x in marks:
    c=c+1
    sum=sum+x
print("total ",sum)
avg=sum/c
print("average ",avg)





























