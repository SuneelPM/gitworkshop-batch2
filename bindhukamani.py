def is_prime(n):
    if num <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print("number is a prime number.")
else:
    print("number is not a prime number.")