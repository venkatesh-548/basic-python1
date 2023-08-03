def cal(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    return a,b,c,d
f=int(input(":"))
g=int(input(":"))
m,n,p,q=cal(f,g)
print(m,n,p,q,end=" ")
    
