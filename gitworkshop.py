def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def printf(n):
    for num in range(2, n + 1):
        if is_prime(num):
            print(num)

# Test the function
n = int(input("Enter a number: "))
printf(n)