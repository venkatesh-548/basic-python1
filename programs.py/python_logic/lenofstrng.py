 #to calculate the length of the string
t="nannapaneni venkata rao college of engineering and technology"
#print(len(t))
def fun(str1):
    count=0
    for char in str1:
        count=count+1
    return count
print(fun(t))
