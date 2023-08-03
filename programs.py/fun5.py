def big(x,y):
    if(x>y):
        return x
    if(x<y):
        return y
    if(x==y):
        print("equal")
print("enter z integer:")
a=int(input())
b=int(input())
c=big(a,b)
print("the result",c)
