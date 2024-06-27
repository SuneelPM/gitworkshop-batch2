def prime(num):
    if num<2:
        return 0
    else:
        x=num
        for j in range(2,x+1):
            if num%j==0:
                return 0
            return 1
a,b=1,100
for i in range(a,b+1):
    if prime(i):
        print(i)
