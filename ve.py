def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
prime_numbers = []
for num in range(1, 101):
    if is_prime(num):
        prime_numbers.append(num)
print("Prime numbers between 1 and 100:")
print(prime_numbers)

