
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?

def prime_factors(n):
	for i in range(2, n+1):
		if n % i == 0:
			return i


print prime_factors(15)
