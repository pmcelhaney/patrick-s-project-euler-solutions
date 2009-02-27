# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6^(th) prime is 13.
#	
# What is the 10001st prime number?

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
        
print primes_up_to(200000)[10000]        
