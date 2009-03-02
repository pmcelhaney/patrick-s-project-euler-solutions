# Problem 12
#
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7^(th) triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The
# first ten terms would be:
#  
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#  
# Let us list the factors of the first seven triangle numbers:
#  
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28
#  
# We can see that 28 is the first triangle number to have over five divisors.
#  
# What is the value of the first triangle number to have over five hundred
# divisors?

import unittest

def all_factors(n):
	i = 1
	if n == 1:
	    yield 1
	max = n / 2 + 1
	while i < max:
	  if n % i == 0:
			yield i
			counterpart = n / i    
			if counterpart != i:
			    yield counterpart
			max = counterpart
	  i = i + 1
	

def factors(n):
    return tuple(all_factors(n))

def triangle_numbers(max=1000000):
    i = 1
    next = 0
    while i <= max:
        next += i
        yield next
        i = i + 1


def first_triangle_number_with_more_than_n_factors(n):
    max = 0
    for i in triangle_numbers():
        count = len(factors(i))
        if  count > n: 
            return i
        #elif count > max:
        #    max = count
        #    print count, i
        
class FactorsTest(unittest.TestCase):
    
    def test_1(self):
        self.assertEquals([1,], sorted(factors(1)))
        
    def test_3(self):
        self.assertEquals([1,3], sorted(factors(3)))
    
    def test_6(self):
        self.assertEquals([1,2,3,6], sorted(factors(6)))    
    
    def test_16(self):
        self.assertEquals([1,2,4,8,16], sorted(factors(16)))    
    
    def test_21(self):
        self.assertEquals([1,3,7,21], sorted(factors(21)))    
    
    def test_28(self):
        self.assertEquals([1,2,4,7,14,28], sorted(factors(28)))    
    

class TriangleNumbersTest(unittest.TestCase):
    def test_first(self):
        next_triangle_number = triangle_numbers(1)
        self.assertEquals([1,], [x for x in next_triangle_number])
        
    def test_first_few(self):
        self.assertEquals((1,3,6,10,15), tuple(triangle_numbers(5)))    

class SolutionTest(unittest.TestCase):
    def test_example(self):
        self.assertEquals(28, first_triangle_number_with_more_than_n_factors(5))
    
if __name__ == '__main__':
    unittest.main()    
    # print first_triangle_number_with_more_than_n_factors(200)
    