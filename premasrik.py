l=1
u=100
for n in range(l,u+1):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
                print(n)
