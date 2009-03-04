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

    def test_collatz_len_one(self):
        self.assertEquals(1, collatz_len(1))
        
    def test_collatz_len_13(self):
        self.assertEquals(10, collatz_len(13))  
        

cache = { 1: 1 }


def collatz_len(n):
    global cache
    if not cache.has_key(n):
        if n % 2 == 0:    
            cache[n] = collatz_len(n / 2) + 1
        else:
            cache[n] = collatz_len(3 * n + 1) + 1
    return cache[n]
        
if __name__ == "__main__":
    #unittest.main()
    map(collatz_len, range(1,1000000))
    print max(cache.keys(), key = lambda k: cache[k]) 