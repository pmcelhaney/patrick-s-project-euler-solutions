# encoding: utf-8
#
# The following iterative sequence is defined for the set of positive
# integers:
#  
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#  
# Using the rule above and starting with 13, we generate the following
# sequence: 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#  
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem), it
# is thought that all starting numbers finish at 1.
#  
# Which starting number, under one million, produces the longest chain?
#  
# NOTE: Once the chain starts the terms are allowed to go above one million.

import unittest

class CollatzTest(unittest.TestCase):
    def testIsOdd(self):
        self.assertTrue(isOdd(1))
        self.assertFalse(isOdd(2))
        self.assertTrue(isOdd(35))
        self.assertFalse(isOdd(0))

    def testCollatzOne(self):
        self.assertEquals([1], collatz(1))
    
    def testCollatzTwo(self):
        self.assertEquals([2, 1], collatz(2))
    
    def testCollatzFour(self):
            self.assertEquals([4, 2, 1], collatz(4))
            
    def testCollatzFive(self):
            self.assertEquals([5,16,8,4, 2, 1], collatz(5))
            
    def testCollatz13(self):
            self.assertEquals([13,40,20,10,5,16,8,4,2,1], collatz(13))                
    
def isOdd(n):
    return n % 2 == 1

def collatz(n):
    if n == 1:
        return [1]
    if isOdd(n):
        return [n] + collatz(3 * n + 1)
    else:
        return [n] + collatz(n/2)
        
if __name__ == "__main__":
    unittest.main()