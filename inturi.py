def prime():
    print("Prime numbers between 1 to 100")
    for i in range(1,101):
        flag=0
        for j in range(1,i+1):
            if(i%j==0):
                flag+=1
        if(flag==2):
            print(i)
prime()
