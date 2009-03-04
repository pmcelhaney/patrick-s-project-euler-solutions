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
    def test_is_odd(self):
        self.assertTrue(is_odd(1))
        self.assertFalse(is_odd(2))
        self.assertTrue(is_odd(35))
        self.assertFalse(is_odd(0))

    def test_collatz_one(self):
        self.assertEquals([1], collatz(1))
    
    def test_collatz_two(self):
        self.assertEquals([2, 1], collatz(2))
    
    def test_collatz_four(self):
        self.assertEquals([4, 2, 1], collatz(4))
            
    def test_collatz_five(self):
        self.assertEquals([5,16,8,4, 2, 1], collatz(5))
            
    def test_collatz_13(self):
        self.assertEquals([13,40,20,10,5,16,8,4,2,1], collatz(13))                

    def test_collatz_len_one(self):
        self.assertEquals(1, collatz_len(1))
        
    def test_collatz_len_13(self):
        self.assertEquals(10, collatz_len(13))  
        
    def test_collatz_len_cached_13(self):
        self.assertEquals(10, collatz_len_cached(13))    

known_collatz_lengths = { 1: 1 }
    
def is_odd(n):
    return n % 2 == 1

def collatz(n):
    if n == 1:
        return [1]
    if is_odd(n):
        return [n] + collatz(3 * n + 1)
    else:
        return [n] + collatz(n/2)

def collatz_len(n):
    if n == 1:
        return 1
    if is_odd(n):
        return 1 + collatz_len(3 * n + 1)
    else:
        return 1 + collatz_len(n/2)

def collatz_len_cached(n):
    if n not in known_collatz_lengths:
        known_collatz_lengths[n] = collatz_len(n)
    return known_collatz_lengths[n]    
        
if __name__ == "__main__":
    #unittest.main()
    map(collatz_len_cached, range(1,1000))
    print max(known_collatz_lengths.keys(), key = lambda k: known_collatz_lengths[k]) 