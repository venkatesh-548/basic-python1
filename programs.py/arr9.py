from array import*
str=input("enter elements with spaces:").split(" ")
marks=[int(num) for num in str]
l=len(marks)
print(l)
sum=0
for i in range(0,l):
    sum=sum+marks[i]
print('total ',sum)
avg=sum/l
print("avg ",avg)














