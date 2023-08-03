n=int(input("enter a number:"))
sqr=pow(n,2)
mod=pow(10,len(str(n)))
if(sqr%mod==n):
    print("automorphic number")
else:
    print('no')
