def isprime(n):
	for i in range(2,n//2):
		if n%i==0:
			return False
	return True

n = int(input("Enter a number to find whether it is prime or not "))

if isprime(n):
	print("YES")
else:
	print("NO")
