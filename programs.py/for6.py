#print prime numbers in the rnge
for n in range(1,101):
    fc=0
    i=1
    while(i<=n):
        if(n%i==0):
            fc=fc+1
        i=i+1
    if(fc==2):
        print(n,end=" ")
