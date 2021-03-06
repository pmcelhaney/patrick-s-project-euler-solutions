# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

def prime_factors(n):
	i = 2
	while i < n:
	
	  if n % i == 0:
			return [i] + prime_factors(n / i)
			
	  i = i + 1
	
	return [n]

print prime_factors(120)