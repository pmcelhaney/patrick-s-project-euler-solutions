# Problem 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# 
# Find the sum of all the primes below two million.


# uses Eratosthenes's Sieve, thanks to Noah
def primes_up_to(max):
  primes = []
  possible_primes = [True for x in xrange(max)]
  
  for i in range(2,max):
    if possible_primes[i]:
      primes.append(i)
      j = i * 2
      while j < max:
        possible_primes[j] = False
        j = j + i 
  
  return primes
        
print sum(primes_up_to(2000000))        




