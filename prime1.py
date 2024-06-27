n=int(input("enter a number "))
def priime(n):
    for i in range(2,101):
        for j in range(2,101):
            if i%j==0:
                print(i)
            else:
                print("not prime")
    
priime(n)