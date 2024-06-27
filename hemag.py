def Prime(number):
    if number<2:
        return 0
    else:
        x=number
        for j in range(2, x + 1):
            if number % j == 0:
                return 0
            return 1


a, b = 1, 100
for i in range(a, b + 1):
    if Prime(i):
        print(i, end=" ")